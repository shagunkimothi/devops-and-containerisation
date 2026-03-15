from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import psycopg2
import os
import time

app = FastAPI(title="Container App")

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 5432),
        dbname=os.getenv("POSTGRES_DB", "appdb"),
        user=os.getenv("POSTGRES_USER", "appuser"),
        password=os.getenv("POSTGRES_PASSWORD", "apppass"),
    )

def init_db():
    for attempt in range(10):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS records (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    message TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT NOW()
                )
            """)
            conn.commit()
            cur.close()
            conn.close()
            print("✅ DB initialised")
            return
        except Exception as e:
            print(f"⏳ DB not ready (attempt {attempt+1}/10): {e}")
            time.sleep(3)
    raise RuntimeError("Could not connect to DB after 10 attempts")

@app.on_event("startup")
def startup():
    init_db()

class Record(BaseModel):
    name: str
    message: str

@app.get("/health")
def health():
    try:
        conn = get_db()
        conn.close()
        return {"status": "ok", "db": "connected"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

@app.post("/records", status_code=201)
def create_record(record: Record):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO records (name, message) VALUES (%s, %s) RETURNING id, name, message, created_at",
        (record.name, record.message)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"id": row[0], "name": row[1], "message": row[2], "created_at": str(row[3])}

@app.get("/records")
def get_records():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, message, created_at FROM records ORDER BY created_at DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1], "message": r[2], "created_at": str(r[3])} for r in rows]

@app.get("/", response_class=HTMLResponse)
def index():
    with open("/app/static/index.html") as f:
        return f.read()

app.mount("/static", StaticFiles(directory="/app/static"), name="static")
