# CONTAINERIZATION AND DEVOPS THEORY

## 25 FEBRUARY 2026  
### Docker Run, Docker Compose & Port Conflict Handling

---

## 📌 Objective

To understand:

- Running containers with advanced Docker options  
- Using Docker Compose  
- Handling port conflicts  
- Viewing logs and managing services  

---

# 🐳 Part 1 — Running NGINX Using Docker

## 🔹 Docker Run Command

```bash
docker run \
  --name my-nginx \
  -p 8080:80 \
  -v ./html:/usr/share/nginx/html \
  -e NGINX_HOST=localhost \
  --restart unless-stopped \
  -d \
  nginx:alpine
```

![Docker Run Output](./1.png)

---

# 🧰 Part 2 — Docker Compose Setup

## 🔹 docker-compose.yml

```yaml
version: '3'

services:
  nginx:
    image: nginx:alpine
    container_name: my-nginx-new
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    restart: unless-stopped
```

![Compose File Execution](./2.png)

---

# ⚠️ Port Conflict Issue

When running:

```bash
docker-compose up -d
```

Error received:

```
Bind for 0.0.0.0:8080 failed: port is already allocated
```

![Port Conflict Error](./3.png)

---

# 🔍 Checking Running Containers

```bash
docker ps
```

Observed that another container was already using port 8080.

![Running Containers](./4.png)

---

# 🛠 Resolving Port Conflict

Stopped and removed the conflicting container:

```bash
docker rm -f my-nginx
```

Then started Docker Compose again:

```bash
docker-compose up -d
```

![Compose Successful Start](./5.png)

---

# 📜 Viewing Logs

```bash
docker-compose logs
```

Logs confirmed that NGINX started successfully.

---

# 📊 Checking Service Status

```bash
docker-compose ps
```

Confirmed that the service was running on:

```
0.0.0.0:8080 -> 80/tcp
```

---

# 🧹 Stopping Services

```bash
docker-compose down
```

This stopped and removed containers along with the default network.

---

# ✅ Conclusion

In this session, we learned:

- How to run containers using advanced `docker run` options  
- How to create and use a `docker-compose.yml` file  
- How to identify and resolve port conflicts  
- How to inspect logs and container status  
- How to properly stop and clean up services  

This experiment demonstrates practical container lifecycle management using Docker and Docker Compose.