# Exp7:CI/CD Demo App

A simple Flask application packaged with Docker and orchestrated with Jenkins.

## Project Overview

This repository contains:
- `app.py`: a minimal Flask web app that returns a greeting at `/`.
- `Dockerfile`: builds a Docker image for the Flask app.
- `docker-compose.yml`: starts a Jenkins server with Docker socket access.
- `Jenkinsfile`: defines a Jenkins pipeline to build and push a Docker image.
- `requirement.txt`: Python dependency listing (`flask`).

## What this project demonstrates

- Running a Python web app in Docker
- Using `docker-compose` to launch Jenkins
- Bootstrapping Jenkins and accessing the initial admin password
- Creating a Jenkins pipeline job (`ci-cd-pipeline`)
- Building and pushing a Docker image from Jenkins

## Files

### `app.py`

A simple Flask app:
- Listens on port `80`
- Exposes `/`
- Returns `Hello from CI/CD Pipeline!`

### `Dockerfile`

Builds a container image using `python:3.10-slim`:
- copies repository files into `/app`
- installs `requirements.txt`
- exposes port `80`
- runs `python app.py`

### `docker-compose.yml`

Defines a single Jenkins service:
- uses `jenkins/jenkins:lts`
- maps host ports `8080` and `50000`
- stores Jenkins data in a Docker volume
- mounts `/var/run/docker.sock` for Jenkins to run Docker commands
- runs as `root`

### `Jenkinsfile`

A declarative pipeline with four stages:
1. `Clone Source`
2. `Build Docker Image`
3. `Login to Docker Hub`
4. `Push to Docker Hub`

> Note: update `IMAGE_NAME`, Git source URL, and Docker Hub credentials before using this pipeline.

## Images

You can link project screenshots or diagrams using Markdown image syntax. Example:

- `![Jenkins startup](1.png)`
- `![Jenkins plugin list](2.png)`
- `![Initial admin password](3.png)`
- `![Jenkins dashboard](4.png)`




## Setup

### 1. Start Jenkins

```bash
docker-compose up -d
```

This will:
- create the default Docker network
- create the `jenkins_home` volume
- pull the `jenkins/jenkins:lts` image
- start Jenkins on `http://localhost:8080`

### 2. Retrieve the initial admin password

Inside the Jenkins container, the initial password is stored at:

```bash
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Use this password to complete the Jenkins setup wizard.

### 3. Complete Jenkins setup

In the Jenkins UI, install the recommended plugins and configure:
- Git
- Pipeline
- Workspace Cleanup
- GitHub Branch Source
- SSH Build Agents
- Docker-related plugins if needed

The repository's sample images show the Jenkins Getting Started and plugin view.

### 4. Create the pipeline job

Create a new pipeline job called `ci-cd-pipeline` and configure it to use the repository's `Jenkinsfile`.

### 5. Run the pipeline

Once configured, run the Jenkins job. It should:
- clone the repository
- build the Docker image
- login to Docker Hub using credentials stored in Jenkins
- push the Docker image to the specified repository

## Running the Flask app manually

Build the image locally:

```bash
docker build -t myapp:latest .
```

Run the container:

```bash
docker run -p 80:80 myapp:latest
```

Open `http://localhost` to see the app response.

## Customize for your environment

Update `Jenkinsfile` with your values:

- `IMAGE_NAME`: your Docker Hub repository, e.g. `your-dockerhub-username/myapp`
- Git clone URL in `Clone Source`
- Jenkins credentials ID for Docker login

## Notes

- The current setup is intended for demonstration and learning.
- Mounting the Docker socket into Jenkins gives the Jenkins container Docker access; use this carefully in production.
- Use a secure Jenkins setup and protected credentials when deploying this pipeline.
