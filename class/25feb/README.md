# CONTAINERIZATION AND DEVOPS THEORY

## 25 FEBRUARY 2026  
### Docker Run, Docker Compose, Port Conflict Handling & Multi-Container Setup

---

## 📌 Objective

- Running containers using advanced Docker options  
- Using Docker Compose  
- Handling port conflicts  
- Viewing logs and managing services  
- Deploying a multi-container WordPress + MySQL stack  

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

### 📷 Output

![Docker Run Output](./1.png)

---

# 🧰 Part 2 — Docker Compose Setup (NGINX)

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

### 📷 Compose Execution

![Compose Execution](./2.png)

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

### 📷 Error Screenshot

![Port Conflict Error](./3.png)

---

# 🔍 Checking Running Containers

```bash
docker ps
```

### 📷 Running Containers

![Running Containers](./4.png)

---

# 🛠 Resolving Port Conflict

```bash
docker rm -f my-nginx
docker-compose up -d
```

### 📷 Successful Start

![Compose Successful Start](./5.png)

---

# 🌐 Part 3 — WordPress + MySQL Using Docker Compose

## 🔹 docker-compose.yml (Multi-Container Setup)

```yaml
version: '3.8'

services:
  mysql:
    image: mysql:5.7
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppass
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - wordpress-network

  wordpress:
    image: wordpress:latest
    container_name: wordpress
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wp_content:/var/www/html/wp-content
    depends_on:
      - mysql
    networks:
      - wordpress-network

volumes:
  mysql_data:
  wp_content:

networks:
  wordpress-network:
```

### 📷 WordPress Compose File

![WordPress Compose File](./6.png)

---

# 🚀 Starting WordPress Stack

```bash
docker-compose up -d
```

### 📷 Compose Up Output

![Compose Up Execution](./7.png)

---

# 📊 Checking Running Services

```bash
docker-compose ps
```

### 📷 Services Running

![Services Running](./8.png)

---

# 📜 Viewing Logs

```bash
docker-compose logs
```

### 📷 Logs Output

![Logs Output](./11.png)

---

# 🌍 Accessing WordPress

Open in browser:

```
http://localhost:8080
```

### 📷 WordPress Setup Page

![WordPress Setup](./10.png)

---

# 🎯 WordPress Dashboard

After completing setup:

### 📷 Final Output

![WordPress Running](./9.png)

---

# 🚀 Key Advantages of Docker Compose

## 1️⃣ Simplicity

Instead of multiple `docker run` commands:

```bash
docker-compose up -d
```

---

## 2️⃣ Reproducibility

- Same configuration everywhere  
- No forgotten flags  
- Consistent environment  

---

## 3️⃣ Declarative Configuration

- Define what you want  
- Self-documenting  
- Easy to modify  

---

## 4️⃣ Lifecycle Management

```bash
docker-compose up    # Start
docker-compose down  # Stop & clean
docker-compose logs  # View logs
docker-compose ps    # Check status
```

---

# 🧠 Key Concepts Learned

- Docker Compose manages multi-container applications  
- Service names act as internal DNS  
- Named volumes provide persistent storage  
- Custom networks isolate services  
- Port conflicts must be handled properly  
- Logs assist debugging  

---

# ✅ Final Conclusion

This experiment demonstrated:

- Single-container deployment using `docker run`  
- Container orchestration using Docker Compose  
- Debugging port conflicts  
- Multi-container WordPress deployment  
- Networking and volume management  

This lab provides practical exposure to real-world container lifecycle management using Docker and Docker Compose.