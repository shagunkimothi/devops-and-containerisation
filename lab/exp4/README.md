# Experiment 4 — Docker Optimization, Inspection & Publishing

## Overview

This experiment demonstrates advanced Docker concepts including:

- Building Flask and Node.js applications
- Multi-stage builds
- Image inspection and history analysis
- Multi-tagging strategies
- Publishing images to Docker Hub
- Comparing cached vs no-cache builds

---

## Prerequisites

- Docker installed and running
- Docker Hub account (username: `shagunkimothi`)
- Python 3 / Node.js source files ready in respective directories

---

## Part 1 — Flask Application

### 1. Build Flask Image

```bash
docker build -t my-flask-app .
```

> Builds the Flask Docker image from the `Dockerfile` in the current directory and tags it as `my-flask-app`.

![Flask Build](build%20flask.png)

---

### 2. Run Flask Container

```bash
docker run -d -p 5000:5000 my-flask-app
```

> Runs the Flask container in detached mode, mapping host port `5000` to container port `5000`.  
> Access the app at: [http://localhost:5000](http://localhost:5000)

![Run Container](run%20container.png)

---

### 3. List Docker Images

```bash
docker images
```

> Displays all locally available Docker images along with their tags, image IDs, creation time, and size.

![Docker Images](docker%20images.png)

---

### 4. Inspect Image

```bash
docker inspect my-flask-app
```

> Returns detailed low-level information about the image in JSON format, including environment variables, entry points, layers, and more.

![Docker Inspect](docker%20inspect%20flaskapp.png)

---

### 5. View Docker History

```bash
docker history my-flask-app
```

> Shows the build history of the image — each layer, the command that created it, and its size. Useful for auditing and optimizing image layers.

![Docker History](docker%20histork%20flaskapp.png)

---

### 6. Tag Image

```bash
docker tag my-flask-app shagunkimothi/my-flask-app:1.0
```

> Tags the local `my-flask-app` image with the Docker Hub repository name and version `1.0`, preparing it for publishing.

---

### 7. Push Image to Docker Hub

```bash
docker push shagunkimothi/my-flask-app:1.0
```

> Uploads the tagged image to the Docker Hub repository at `shagunkimothi/my-flask-app`.

---

### 8. Pull Image from Docker Hub

```bash
docker pull shagunkimothi/my-flask-app:1.0
```

> Downloads the published image from Docker Hub. Anyone with access can pull and run the image.

---

## Part 2 — Node.js Application

### 1. Build Node Image

```bash
docker build -t my-node-app .
```

> Builds the Node.js Docker image from the `Dockerfile` in the current directory.

![Node Build](node%20app%20build.png)

---

### 2. Run Node Container

```bash
docker run -d -p 3000:3000 my-node-app
```

> Runs the Node.js container in detached mode, mapping host port `3000` to container port `3000`.  
> Access the app at: [http://localhost:3000](http://localhost:3000)

![Run Node](run%20and%20test%20node%20container.png)

---

### 3. Multi-Tag Build

```bash
docker build \
  -t my-node-app:latest \
  -t myapp:v2.0 \
  -t shagunkimothi/my-node-app:production \
  .
```

> Builds the image once and assigns multiple tags simultaneously — useful for versioning, aliasing, and publishing in a single command.

---

### 4. Multi-Stage Build

```bash
docker build -t my-node-app:multistage .
```

> Uses a multi-stage `Dockerfile` to separate the build environment from the production image. This significantly reduces the final image size by excluding build tools and intermediate dependencies.

![Node Multistage](node%20multistage.png)

---

### 5. Build Without Cache

```bash
docker build --no-cache -t clean-app .
```

> Forces Docker to rebuild every layer from scratch, ignoring cached intermediate layers. Ensures a completely fresh build — useful for debugging or verifying reproducibility.

![Clean Build](clean%20build%20node.png)

---

### 6. Compare Cached Build

```bash
time docker build -t cached-app .
```

> Times the build process using Docker's layer cache. Cached builds are significantly faster since unchanged layers are reused. Compare the elapsed time with the `--no-cache` build above.

![Cached Build](compare%20cache%20build%20node.png)

---

### 7. Manage Containers

```bash
# List running containers
docker ps

# Stop a running container
docker stop <container_id>

# Remove a stopped container
docker rm <container_id>
```

> Standard container lifecycle commands. Replace `<container_id>` with the actual ID shown in `docker ps`.

![Manage Containers](manage%20containers.png)

---

## Key Concepts Summary

| Concept | Command | Purpose |
|---|---|---|
| Build image | `docker build -t <name> .` | Create image from Dockerfile |
| Run container | `docker run -d -p <host>:<container> <image>` | Start container in background |
| List images | `docker images` | View all local images |
| Inspect image | `docker inspect <image>` | Detailed image metadata |
| View history | `docker history <image>` | Layer-by-layer build history |
| Tag image | `docker tag <src> <dst>` | Alias image for publishing |
| Push to Hub | `docker push <tag>` | Publish image to Docker Hub |
| Pull from Hub | `docker pull <tag>` | Download image from Docker Hub |
| Multi-tag | `docker build -t a -t b .` | Assign multiple tags at build |
| Multi-stage | Multi `FROM` in Dockerfile | Smaller, cleaner production images |
| No-cache build | `docker build --no-cache` | Fresh rebuild, ignore cache |
| Timed build | `time docker build ...` | Measure build duration |
| Stop container | `docker stop <id>` | Gracefully stop container |
| Remove container | `docker rm <id>` | Delete stopped container |

---

## Conclusion

This experiment demonstrates Docker optimization techniques and best practices:

- **Multi-stage builds** reduce final image size by separating build and runtime environments.
- **Layer caching** dramatically speeds up rebuilds when source files haven't changed.
- **`docker inspect` and `docker history`** are powerful tools for auditing image configuration and layer structure.
- **Multi-tagging** allows a single build to be simultaneously versioned, aliased, and prepared for production publishing.
- **Docker Hub** serves as the central registry for sharing and distributing images across environments and teams.