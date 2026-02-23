# CONTAINERIZATION AND DEVOPS THEORY

## 28 JANUARY 2026  
### Building a Java Application using Dockerfile

---

## 📌 Objective

To containerize a Java application using a Dockerfile and execute it inside a Docker container.

---

## 🧱 Dockerfile Used

```dockerfile
FROM openjdk:17-jdk-slim

WORKDIR /app

COPY HelloWorld.java .

RUN javac HelloWorld.java

CMD ["java", "HelloWorld"]
```

---

## 🔹 Step 1 — Build the Docker Image

```bash
docker build -t java-app .
```

[View Build Output Screenshot](./1.png)

---

## 🔹 Step 2 — Verify Image Creation

```bash
docker images
```

[View Docker Images Screenshot](./2.png)

---

## 🔹 Step 3 — Run the Docker Container

```bash
docker run java-app
```

[View Container Execution Screenshot](./3.png)

---

## 🔹 Step 4 — Verify Application Output

[View Application Output Screenshot](./4.png)

---

## ✅ Conclusion

- Dockerfile was created successfully  
- Docker image was built  
- Container was executed  
- Java application output was verified  

This experiment demonstrates the process of containerizing a Java application using Docker.