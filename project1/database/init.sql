CREATE TABLE IF NOT EXISTS records (
    id         SERIAL PRIMARY KEY,
    name       TEXT        NOT NULL,
    message    TEXT        NOT NULL,
    created_at TIMESTAMP   DEFAULT NOW()
);
