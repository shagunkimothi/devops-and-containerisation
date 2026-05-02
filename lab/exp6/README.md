# Lab 6 — Docker and Compose Exercises

## Overview
This lab explores container fundamentals through multiple parts:
- single container deployment with `docker run`
- Compose-based service definition for nginx and WordPress
- building a custom Node.js app image
- multi-container orchestration with persistent storage

The workspace contains:
- `docker-compose.yml` — top-level Compose configuration for a local Node app build
- `Part B/` — WordPress and MySQL Compose example
- `Part C/Task 4/` — Node.js app and Dockerfile for custom build
- `Part D/Task 5/` — MySQL persistent volume example
- `html/` — mounted static site directory for nginx
- image files for lab evidence and results

---

## Part 1 — Single Container Comparison
This section compares running nginx directly with `docker run` versus using `docker-compose`.

### Step 1: Run nginx with `docker run`
```bash
docker run -d \
  --name lab-nginx \
  -p 8081:80 \
  -v "${PWD}/html:/usr/share/nginx/html" \
  nginx:alpine
```

Verify the container is running:
```bash
docker ps
```

Open in browser:
```bash
http://localhost:8081
```

Stop and remove the container:
```bash
docker stop lab-nginx
docker rm lab-nginx
```

### Step 2: Run nginx with `docker-compose`
Create or use the Compose file:
```yaml
version: '3.8'

services:
  nginx:
    image: nginx:alpine
    container_name: lab-nginx
    ports:
      - "8081:80"
    volumes:
      - ./html:/usr/share/nginx/html
```

Run the Compose app:
```bash
docker compose up -d
```

Verify service status:
```bash
docker compose ps
```

Stop the service:
```bash
docker compose down
```

---

## Part 2 — Multi-Container Application
This section demonstrates WordPress with MySQL using both `docker run` and `docker-compose`.

### Task 2A: Run with `docker run`
Create a custom network:
```bash
docker network create wp-net
```

Run MySQL:
```bash
docker run -d \
  --name mysql \
  --network wp-net \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=wordpress \
  mysql:5.7
```

Run WordPress:
```bash
docker run -d \
  --name wordpress \
  --network wp-net \
  -p 8082:80 \
  -e WORDPRESS_DB_HOST=mysql \
  -e WORDPRESS_DB_PASSWORD=secret \
  wordpress:latest
```

Open in browser:
```bash
http://localhost:8082
```

### Task 2B: Run with `docker-compose`
Use the Compose file in `Part B/docker-compose.yml`:
```yaml
version: '3.8'

services:
  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: wordpress
    volumes:
      - mysql_data:/var/lib/mysql

  wordpress:
    image: wordpress:latest
    ports:
      - "8082:80"
    environment:
      - WORDPRESS_DB_HOST=mysql
      - WORDPRESS_DB_PASSWORD=secret
    depends_on:
      - mysql

volumes:
  mysql_data:
```

Start the stack:
```bash
docker compose up -d
```

Stop and remove volumes:
```bash
docker compose down -v
```

---

## Part 3 — Custom Node.js Build (`Part C/Task 4`)
This part builds a simple Express app into a Docker image.

### Files involved
- `Part C/Task 4/Dockerfile`
- `Part C/Task 4/server.js`
- `Part C/Task 4/package.json`

### Dockerfile
```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5000

CMD ["node", "server.js"]
```

### server.js
```js
const express = require('express');
const app = express();
const port = 5000;

app.get('/', (req, res) => {
  res.send('Hello from your Custom Docker Build!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
```

### Build and run
```bash
docker build -t lab-node-app "Part C/Task 4"

docker run -d -p 5000:5000 --name lab-node-app lab-node-app
```

Verify by opening:
```bash
http://localhost:5000
```

Cleanup:
```bash
docker stop lab-node-app
docker rm lab-node-app
docker image rm lab-node-app
```

---

## Part 4 — Persistent MySQL Volume (`Part D/Task 5`)
This task shows a Compose service with a named volume for MySQL data persistence.

### Files involved
- `Part D/Task 5/docker-compose.yml`
- `Part D/Task 5/Dockerfile`
- `Part D/Task 5/app.js`

### docker-compose.yml
```yaml
version: '3.8'

services:
  db:
    image: mysql:5.7
    container_name: mysql-persistent
    environment:
      MYSQL_ROOT_PASSWORD: labpassword
      MYSQL_DATABASE: inventory
    volumes:
      - db_data:/var/lib/mysql
    restart: always

volumes:
  db_data:
```

### app.js
```js
const http = require('http');

http.createServer((req, res) => {
  res.end('Docker Compose Build Lab');
}).listen(3000);
```

### Dockerfile
```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY app.js .

EXPOSE 3000

CMD ["node", "app.js"]
```

Start the database stack:
```bash
docker compose -f "Part D/Task 5/docker-compose.yml" up -d
```

Stop and remove the stack:
```bash
docker compose -f "Part D/Task 5/docker-compose.yml" down -v
```

---

## Image Gallery
The following images document the lab execution and results:

### nginx docker run setup
![Step 1](./step%201.png)

### nginx docker-compose setup
![Step 2](./step%202.png)

### WordPress/MySQL Compose result
![Part B](./part%20B.png)

### WordPress/MySQL using docker run
![Docker Run](./using%20docker%20run.png)

### Persistent volume outcome
![Task 5.1](./task%205.1.png)

---

## Notes
- The root `docker-compose.yml` in `lab/exp6` is configured to build a Node app from a local Dockerfile.
- If that Dockerfile is not present in the root folder, use the `Part C/Task 4` or `Part D/Task 5` examples as working references for custom builds.
- Use `docker compose ps`, `docker ps`, and `docker logs <container>` for troubleshooting.

