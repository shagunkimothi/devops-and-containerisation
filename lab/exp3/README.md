# NGINX Docker Image Comparison Lab

A hands-on DevOps lab demonstrating how different base images impact Docker image size, performance, security, and layers using **NGINX**.

---

## Project Objective

This project explores:

- Deploying NGINX using the official image
- Building custom NGINX images using Ubuntu and Alpine
- Understanding Docker image layers
- Comparing performance, size, and security implications

---




## Part 1 — Run Official NGINX Image

### Pull Image
```bash
docker pull nginx:latest
```

### Run Container
```bash
docker run -d --name nginx-official -p 8080:80 nginx
```

### Verify
Open:
```
http://localhost:8080
```

---

## Part 2 — Build NGINX Using Ubuntu Base

### Dockerfile
```dockerfile
FROM ubuntu:22.04

RUN apt update && apt install -y nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Build
```bash
docker build -t nginx-ubuntu .
```

### Run
```bash
docker run -d --name nginx-ubuntu -p 8081:80 nginx-ubuntu
```

---

## Part 3 — Build NGINX Using Alpine Base

### Dockerfile
```dockerfile
FROM alpine:3.19

RUN apk add --no-cache nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### Build
```bash
docker build -t nginx-alpine .
```

### Run
```bash
docker run -d --name nginx-alpine -p 8082:80 nginx-alpine
```

---

## Image Size Comparison

```bash
docker images
```

| Image | Base OS | Approx Size |
|-------|---------|-------------|
| nginx | Official | Medium |
| nginx-ubuntu | Ubuntu | Large |
| nginx-alpine | Alpine | Small |

---

## Inspect Image Layers

```bash
docker history nginx
docker history nginx-ubuntu
docker history nginx-alpine
```

Each Dockerfile command creates a new layer. More OS packages = larger layers.

---

## Performance & Security Comparison

| Feature | Official | Ubuntu | Alpine |
|--------|----------|--------|--------|
| Size | Medium | Large | Small |
| Security | Good | More attack surface | Minimal |
| Speed | Fast | Moderate | Fastest |
| Use Case | Default | Full OS apps | Cloud-native apps |

---

## Conclusion

This lab proves that base image selection significantly affects Docker image size, security posture, and deployment efficiency. Alpine-based images are ideal for microservices and cloud environments, while Ubuntu provides flexibility for complex applications. Official images offer a balanced, production-ready setup.

---

## Cleanup

```bash
docker stop nginx-official nginx-ubuntu nginx-alpine
docker rm nginx-official nginx-ubuntu nginx-alpine
```

---

Built for learning DevOps, Containers, and Cloud-Native best practices.




