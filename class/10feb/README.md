"# Class Notes" 
# C Application in Docker

This project demonstrates how to containerize a simple C program using Docker.  
The program prints **"Hello, World!"** when executed inside the container.

---

## 📂 Project Structure



- **hello.c** → Source code for the C program.  
- **Dockerfile** → Instructions to build the Docker image.

---

## 🛠️ Prerequisites
- Docker installed and running
- WSL (Windows Subsystem for Linux) or Linux terminal access
- Basic knowledge of Docker commands

---

## 🚀 Steps to Run

### 1. Navigate to the Project Directory
```bash
cd "/mnt/d/devops and containerisation/class/10feb"
docker build -t c-app:1.0 .
docker run -it c-app:1.0
