# Experiment 5 : Docker - Volumes, Environment Variables, Monitoring & Networks

# Part 1 : Docker Volumes - Persistent Data Storage

## Lab 1 : Understanding Data Persistence
```bash
# Create a container that writes data
docker run -it --name test-container ubuntu /bin/bash

# Inside container:
echo "Hello World" > /data/message.txt
cat /data/message.txt  # Shows "Hello World"
exit

# Restart container
docker start test-container
docker exec test-container cat /data/message.txt
# ERROR: File doesn't exist! Data was lost.
```
![Container](1.png)

---

## Lab 2 : Volume Types

### 1. Anonymous Volumes
```bash
# Create anonymous volume (auto-generated name)
docker run -d -v /app/data --name web1 nginx

# Check volume
docker volume ls
# Shows: anonymous volume with random hash

# Inspect container to see volume mount
docker inspect web1 | grep -A 5 Mounts
```
![volume](2.png)

---

### 2. Named Volume
```bash
# Create named volume
docker volume create mydata

# Use named volume
docker run -d -v mydata:/app/data --name web2 nginx

# List volumes
docker volume ls
# Shows: mydata

# Inspect volume
docker volume inspect mydata
```
![named volume](named%20volume.png)

---

### 3. Bind Volume
```bash
# Create directory on host
mkdir ~/myapp-data

# Mount host directory to container
docker run -d -v ~/myapp-data:/app/data --name web3 nginx

# Add file on host
echo "From Host" > ~/myapp-data/host-file.txt

# Check in container
docker exec web3 cat /app/data/host-file.txt
# Shows: From Host
```
![bind mounts](bind%20mount.png)

---

## Lab 3 : Practical Volume Example

### Example 1 : Database with Persistent Storage
```bash
# MySQL with named volume
docker run -d \
  --name mysql-db \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# Check data persists
docker stop mysql-db
docker rm mysql-db
```
![stop volume container](stop%20volume%20container.png)
```bash
# New container with same volume
docker run -d \
  --name new-mysql \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0
# Data is preserved!
```
![example 1](database%20with%20presistent%20storage.png)

---

### Example 2 : Web App with Configuration Files
```bash
# Create config directory
mkdir ~/nginx-config

# Create nginx config file
echo 'server {
    listen 80;
    server_name localhost;
    location / {
        return 200 "Hello from mounted config!";
    }
}' > ~/nginx-config/nginx.conf

# Run nginx with config bind mount
docker run -d \
  --name nginx-custom \
  -p 8080:80 \
  -v ~/nginx-config/nginx.conf:/etc/nginx/conf.d/default.conf \
  nginx

# Test
curl http://localhost:8080
```
![web app](web%20app.png)

---

## Lab 4 : Volume Management
```bash
# List all volumes
docker volume ls

# Create a volume
docker volume create app-volume

# Inspect volume details
docker volume inspect app-volume

# Remove unused volumes
docker volume prune

# Remove specific volume
docker volume rm volume-name

# Copy files to/from volume
docker cp local-file.txt container-name:/path/in/volume
```
![Volume management](volume%20management.png)

---

# Part 2 : Environment Variables

## Lab 1 : Setting Environment Variables

### Method 1 : Using -e Flag
```bash
# Single variable
docker run -d \
  --name app1 \
  -e DATABASE_URL="postgres://user:pass@db:5432/mydb" \
  -e DEBUG="true" \
  -p 3000:3000 \
  my-node-app
```
![Single Variable](single%20variable.png)
```bash
# Multiple variables
docker run -d \
  -e VAR1=value1 \
  -e VAR2=value2 \
  -e VAR3=value3 \
  my-app
```

---

### Method 2 : Using --env-file
```bash
# Create .env file
echo "DATABASE_HOST=localhost" > .env
echo "DATABASE_PORT=5432" >> .env
echo "API_KEY=secret123" >> .env

# Use env file
docker run -d \
  --env-file .env \
  --name app2 \
  my-app

# Use multiple env files
docker run -d \
  --env-file .env \
  --env-file .env.secrets \
  my-app
```
![part 2](part2.1.png)
![part 2](part2.2.png)

---

### Method 3 : In Dockerfile

![build](build.png)

---

## Lab 2 : Environment Variable - Python Flask Example

![flask app](flask%20app.png)
![docker image](docker%20image.png)

---

## Lab 3 : Test Environment
```bash
# Run with custom env vars
docker run -d \
  --name flask-app \
  -p 5000:5000 \
  -e DATABASE_HOST="prod-db.example.com" \
  -e DEBUG="true" \
  -e PORT="8080" \
  flask-app

# Check environment in running container
docker exec flask-app env
docker exec flask-app printenv DATABASE_HOST

# Test the endpoint
curl http://localhost:5000/config
```
![run custom env](run%20custom%20env.png)
![test endpoint](test%20endpoint.png)

---

# Part 3 : Docker Monitoring

## Lab 1 : Basic Monitoring Commands

### Important - Start Container First

docker stats only shows **running** containers. If all containers are stopped, output will be empty.
```bash
# Check running containers
docker ps

# If empty, start your containers first
docker start flask-app
docker start nginx-custom

# Verify they are running
docker ps
```
```
# Empty stats output (all containers stopped)
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
                                                                    ← no rows = no running containers
```

---

### Commands
```bash
# Live stats for all running containers
docker stats
```
![docker stats](docker%20stats.png)
```bash
# Single snapshot (no live stream)
docker stats --no-stream
```
![docker live stats](docker%20live%20stats.png)
```bash
# All containers including stopped (shows 0s for stopped)
docker stats --all
```
```bash
# Specific containers
docker stats flask-app nginx-custom
```
```bash
# Custom format
docker stats --format "Container: {{.Name}} | CPU: {{.CPUPerc}} | Memory: {{.MemPerc}}"
```
![Custom](custom%20format.png)
```bash
# JSON output
docker stats --format json --no-stream
```
![json](json%20format.png)
```bash
# Wide output
docker stats --no-stream --no-trunc
```
![wide](wide%20output.png)
```bash
# Table format
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}"
```

---

### Actual Output From Our Containers
```
CONTAINER ID   NAME           CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O   PIDS
8bf09959b660   flask-app      0.25%     44.41MiB / 7.418GiB   0.58%     1.52kB / 126B   0B / 0B     3
b8886bbce86c   nginx-custom   0.00%     17.73MiB / 7.418GiB   0.23%     726B / 126B     0B / 0B     17
```

---

### Stats Output Columns

| Column | flask-app | nginx-custom | Meaning |
|---|---|---|---|
| CPU % | 0.25% | 0.00% | Share of total host CPU |
| MEM USAGE | 44.41MiB | 17.73MiB | RAM currently consumed |
| MEM LIMIT | 7.418GiB | 7.418GiB | Max RAM (your host RAM) |
| MEM % | 0.58% | 0.23% | MEM USAGE ÷ LIMIT |
| NET I/O | 1.52kB / 126B | 726B / 126B | Network received / sent |
| BLOCK I/O | 0B / 0B | 0B / 0B | Disk read / written |
| PIDs | 3 | 17 | Processes inside container |

---

### Format Variables Reference

| Variable | Description |
|---|---|
| `{{.Name}}` | Container name |
| `{{.CPUPerc}}` | CPU percentage |
| `{{.MemUsage}}` | Memory used / limit |
| `{{.MemPerc}}` | Memory percentage |
| `{{.NetIO}}` | Network in / out |
| `{{.BlockIO}}` | Disk read / write |
| `{{.PIDs}}` | Process count |

---

### Key Observations
- flask-app uses more RAM (44MB) than nginx (17MB) — Python vs C-based nginx
- nginx has 17 PIDs vs flask's 3 — nginx spawns multiple worker processes
- BLOCK I/O is 0 — neither container did any disk reads/writes
- MEM LIMIT shows full host RAM (7.418GiB) — no memory cap set

### For Production Always Set Resource Limits
```bash
docker run -m 256m --cpus="0.5" flask-app
```

---

## Lab 2 : Docker Top - Process Monitoring
```bash
# View processes in container
docker top container-name

# View with full command line
docker top container-name -ef

# Compare with host processes
ps aux | grep docker
```
![docker top](docker%20top.png)

---

## Lab 3 : Docker Logs - Application Logs
```bash
# View logs
docker logs container-name
```
![Docker logs](basic%20logs%20flask-app.png)
```bash
# Follow logs (like tail -f)
docker logs -f container-name
```
![follow logs](follow%20logs%20flask-app.png)
```bash
# Last N lines
docker logs --tail 100 container-name
```
![last n lines](last%20N%20fines%20flask-app.png)
```bash
# Logs with timestamps
docker logs -t container-name
```
![timestamp](logs%20timestamp%20flask-app.png)
```bash
# Logs since specific time
docker logs --since 2024-01-15 container-name
```
![specific time](logs%20specific%20time%20flask-app.png)
```bash
# Combine options
docker logs -f --tail 50 -t container-name
```
![combine](combine%20option%20flask%20app.png)

---

## Lab 4 : Container Inspection
```bash
# Detailed container info
docker inspect flask-app
```
![Docker inspect](docker%20inspect%20flask-app.png)
```bash
# Container state
docker inspect --format='{{.State.Status}}' flask-app
# running

# IP Address
docker inspect --format='{{.NetworkSettings.IPAddress}}' flask-app
# 172.17.0.2

# Environment variables
docker inspect --format='{{.Config.Env}}' flask-app
# [PATH=/usr/local/bin FLASK_ENV=development ...]

# Image used
docker inspect --format='{{.Config.Image}}' flask-app
# flask-app

# Container start time
docker inspect --format='{{.State.StartedAt}}' flask-app
# 2026-02-28T16:08:10Z

# Port mappings
docker inspect --format='{{.HostConfig.PortBindings}}' flask-app
# map[5000/tcp:[{ 5000}]]

# Mounted volumes
docker inspect --format='{{.Mounts}}' flask-app
```
![Inspect specific information](inspect%20specific%20info.png)
```bash
# Memory limit (0 = no limit)
docker inspect --format='{{.HostConfig.Memory}}' flask-app
# 0

# CPU limit (0 = no limit)
docker inspect --format='{{.HostConfig.NanoCpus}}' flask-app
# 0

# CPU shares
docker inspect --format='{{.HostConfig.CpuShares}}' flask-app
# 0
```
![Resource limit](resource%20limit.png)

---

## Lab 5 : Events Monitoring

Stream real-time events from the Docker daemon.
```bash
# Listen for all events
docker events
```
```bash
# Filter by type/action
docker events --filter 'type=container'
docker events --filter 'event=start'
docker events --filter 'event=die'
```
```bash
# Check recent history
docker events --since '10m'
```
```bash
# Clean formatted output
docker events --format '{{.Type}} {{.Action}} {{.Actor.Attributes.name}}'
```
```bash
# Run listener in background, trigger events, then stop listener
docker events --filter 'type=container' &
docker restart flask-app
kill %1
```
![event monitoring](events%20monitoring.png)
![event monitoring 2](event%20monitoring%202.png)

### Container Restart Lifecycle
```
kill (signal=15) → network disconnect → stop → die → network connect → start → restart
```

### Event Types Reference

| Type | Common Actions |
|---|---|
| container | create, start, stop, die, kill, restart, oom |
| image | pull, push, tag, delete |
| network | connect, disconnect, create, destroy |
| volume | create, mount, unmount, destroy |

---

## Lab 6 : Practical Monitoring Script

### monitor.sh - Simple Docker Monitoring Dashboard
```bash
#!/bin/bash
echo "=== Docker Monitoring Dashboard ==="
echo "Time: $(date)"
echo

echo "1. Running Containers:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo

echo "2. Resource Usage:"
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}"
echo

echo "3. Recent Events:"
docker events --since 5m --until 0s --format "{{.Time}} {{.Type}} {{.Action}}" | tail -5
echo

echo "4. System Info:"
docker system df
```

---

### How to Create the File
```bash
cat > monitor.sh << 'EOF'
#!/bin/bash
echo "=== Docker Monitoring Dashboard ==="
echo "Time: $(date)"
echo
echo "1. Running Containers:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo
echo "2. Resource Usage:"
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}"
echo
echo "3. Recent Events:"
docker events --since 5m --until 0s --format "{{.Time}} {{.Type}} {{.Action}}" | tail -5
echo
echo "4. System Info:"
docker system df
EOF
```

### How to Run
```bash
# Give execute permission
chmod +x monitor.sh

# Start containers first
docker start flask-app

# Run the script
./monitor.sh
```
![practical monitoring script](practical%20monitoring%20script.png)

---

### Actual Output

![output](output.png)

---

### What Each Section Does

| Section | Command Used | Purpose |
|---|---|---|
| Running Containers | `docker ps` | Shows name, status, ports |
| Resource Usage | `docker stats --no-stream` | Snapshot of CPU, memory, network, disk |
| Recent Events | `docker events --since 5m` | Events in past 5 minutes |
| System Info | `docker system df` | Disk usage across images, containers, volumes |

---

### Notes
- `--no-stream` in stats gives one-time snapshot — perfect for scripts
- `--until 0s` in events prevents the command from hanging
- `tail -5` limits events to last 5 lines
- Recent Events section will be empty if no Docker activity in last 5 minutes
- Run with watch to auto-refresh every 5 seconds:
```bash
watch -n 5 ./monitor.sh
```

---

# Part 4 : Docker Networks

## Lab 1 : Understanding Docker Network Types
```bash
# Default networks
docker network ls
```
![Network types](network%20type.png)

---

## Lab 2 : Network Types Explained

### 1. Bridge Network (Default)
```bash
# Create custom bridge network
docker network create my-network
```
![network](create%20network.png)
```bash
# Inspect network
docker network inspect my-network

# Run containers on custom network
docker run -d --name web1 --network my-network nginx
docker run -d --name web2 --network my-network nginx
```
![custom network](custom%20network.png)
```bash
# Containers can communicate using container names
docker exec web1 curl http://web2
```

---

### 2. Host Network
```bash
# Container uses host's network directly
docker run -d --name host-app --network host nginx

# Access directly on host port 80
curl http://localhost
```
![Host Network](host%20network.png)

---

### 3. None Network
```bash
# No network access
docker run -d --name isolated-app --network none alpine sleep 3600

# Test - no network interfaces
docker exec isolated-app ifconfig
# Only loopback interface
```
![none network](none%20network.png)

---

### 4. Overlay Swarm
```bash
# For Docker Swarm - multi-host networking
docker network create --driver overlay my-overlay
```
![overlay network](overlay%20network.png)

---

## Lab 3 : Network Management

### 1. Create Networks
```bash
# Create a basic bridge network
docker network create app-network
```
![network](create%20app-network.png)
```bash
# Create network with custom subnet and gateway
docker network create --driver bridge --subnet 172.25.0.0/16 --gateway 172.25.0.1 my-subnet
```

> ⚠️ If you get `Pool overlaps` error, check existing subnets first:
> ```bash
> docker network inspect $(docker network ls -q) | grep -A3 "Subnet"
> ```
> Then pick a subnet not already in use.

---

### 2. List and Inspect Networks
```bash
# List all networks
docker network ls

# Inspect a specific network
docker network inspect my-network
```
![subnet check](subnet%20check.png)

---

### 3. Connect and Disconnect Containers
```bash
# Connect running container to a network
docker network connect app-network flask-app

# Disconnect container from a network
docker network disconnect app-network flask-app
```

> ⚠️ Container must exist — `existing-container` gave error because no such container was found

---

### 4. Remove Networks
```bash
# Remove a specific network (must have no connected containers)
docker network rm app-network

# Remove all unused networks
docker network prune
```
![output](output%20network.png)

---

### Network Drivers Reference

| Driver | Use Case |
|---|---|
| `bridge` | Default — containers on same host |
| `host` | Container shares host network |
| `overlay` | Multi-host / swarm networking |
| `ipvlan` | Full control over IP addressing |
| `none` | No networking |

---

### Notes
- `docker network create` without `--driver` defaults to `bridge`
- `network prune` only removes networks with **no containers attached**
- Each custom network gets its own subnet automatically if not specified
- Containers on the same network can communicate using container names as hostnames

---

## Lab 4 : Multi Container Application Example
```bash
# Create network
docker network create app-network

# Start database
docker run -d \
  --name postgres-db \
  --network app-network \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15
```
![database](start%20database.png)
```bash
# Start web application
docker run -d \
  --name web-app \
  --network app-network \
  -p 8080:3000 \
  -e DATABASE_URL="postgres://postgres:secret@postgres-db:5432/mydb" \
  -e DATABASE_HOST="postgres-db" \
  node-app
```
![start webapplication](start%20webapplication.png)

---

## Lab 5 : Network Inspection and Debugging
```bash
# Inspect network
docker network inspect bridge
```
```bash
# Check container IP
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' flask-app
```
```bash
# DNS resolution test (nslookup not available in slim images, use alpine)
docker run --rm --network app-network alpine nslookup flask-app
```
```bash
# Network connectivity test
docker run --rm --network app-network alpine ping -c 4 google.com
docker exec nginx-custom curl -I http://flask-app:5000
```
```bash
# View network ports
docker port flask-app
docker port nginx-custom
```

---

### Actual Output From Our Containers
```bash
# flask-app was only on default bridge network
docker inspect flask-app | grep -A5 "Networks"

# Output:
"Networks": {
    "bridge": {
        "IPAMConfig": null,
        "Links": null,
        "Aliases": null,
        "MacAddress": "16:a5:57:39:7a:37"
```

### Output
![output 1](output1.png)
![output 2](output2.png)
![output 3](output3.png)
![output 4](output4.png)
![output 5](output5.png)

---

### Issues Faced and Fixes

| Command | Issue | Fix |
|---|---|---|
| `docker exec flask-app ping` | ping not found in slim image | Use alpine container |
| `docker exec flask-app nslookup` | nslookup not found in slim image | Use alpine container |
| `docker exec nginx-custom curl http://flask-app` | Could not resolve host | Connect both to same custom network |
```bash
# Fix — connect both containers to app-network
docker network connect app-network flask-app
docker network connect app-network nginx-custom

# Then test using alpine
docker run --rm --network app-network alpine ping -c 2 flask-app
docker run --rm --network app-network alpine ping -c 4 google.com
```

---

### Key Notes
- `ping` and `nslookup` are not available in slim images — always use alpine for network debugging
- Default `bridge` network does not support DNS by container name
- Custom networks support DNS — containers can reach each other by name
- Always ensure containers are on the same network before testing connectivity

---

## Lab 6 : Port Publishing
```bash
# Basic port publishing (host:container)
docker run -d -p 8082:80 --name app1 nginx
# Host port 8082 → Container port 80
```
```bash
# Dynamic port publishing (Docker assigns random host port)
docker run -d -p 8083:80 --name app2 nginx
```
```bash
# Multiple ports
docker run -d -p 8084:80 -p 8085:443 --name app3 nginx
```
```bash
# Specific host IP (only localhost can access)
docker run -d -p 127.0.0.1:8086:80 --name app4 nginx
```
```bash
# Check assigned ports
docker port app1
docker port app2
docker port app3
docker port app4
```
```bash
# View all containers with ports
docker ps --format "table {{.Names}}\t{{.Ports}}"
```
![port](post%20exposing.png)

---

### Issues Faced and Fixes
```bash
# Error 1 — Port already in use
docker run -d -p 80:8080 --name app1 nginx
# Error: address already in use
# Fix — check used ports first
docker ps --format "table {{.Names}}\t{{.Ports}}" | grep :80
# Then use a free port like 8082
```
```bash
# Error 2 — Container name conflict
docker run -d -p 8082:80 --name app1 nginx
# Error: container name already in use
# Fix — remove failed container first
docker rm app1
docker run -d -p 8082:80 --name app1 nginx
```

---

### Port Publishing Format
```
-p host_ip:host_port:container_port
-p host_port:container_port        ← most common
-p container_port                  ← random host port
```

| Container | Host Port | Container Port | Accessible From |
|---|---|---|---|
| app1 | 8082 | 80 | everywhere |
| app2 | 8083 | 80 | everywhere |
| app3 | 8084, 8085 | 80, 443 | everywhere |
| app4 | 8086 | 80 | localhost only |

---

### EXPOSE vs -p

| | `EXPOSE` in Dockerfile | `-p` in docker run |
|---|---|---|
| Purpose | Documentation only | Actually publishes port |
| Accessible from host | ❌ No | ✅ Yes |
| Required to publish | No | Yes |
```dockerfile
# Dockerfile — EXPOSE is metadata only
EXPOSE 80
# Still need -p flag when running:
# docker run -p 8082:80 nginx
```

---

### Key Notes
- Each host port can only be used by **one container at a time**
- `EXPOSE` in Dockerfile does NOT publish the port — `-p` is always required
- Without `-p`, container is only accessible from other containers on same network
- Use `127.0.0.1:host_port:container_port` to restrict access to localhost only
- Always check used ports before running: `docker ps --format "table {{.Names}}\t{{.Ports}}"`
- Always remove failed containers before reusing name: `docker rm container-name`

---

# Part 5 : Multi-Container Application Setup

### Overview
Connect multiple containers (PostgreSQL + Redis + Flask) on a custom network with volumes and environment variables.

---

### Step 1 - Create Network
```bash
docker network create myapp-network
```

---

### Step 2 - Start PostgreSQL Database
```bash
docker run -d \
  --name postgres \
  --network myapp-network \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=mydatabase \
  -v postgres-data:/var/lib/postgresql/data \
  postgres:15
```
![step 2](step%202.png)

---

### Step 3 - Start Redis
```bash
docker run -d \
  --name redis \
  --network myapp-network \
  -v redis-data:/data \
  redis:7-alpine
```
![step 3](step%203.png)

---

### Step 4 - Prepare App Files
```bash
# Check app folder contents
ls app/
ls flask-app/

# Copy app.py to app folder
cp flask-app/app.py app/

# Verify
ls app/
```
![step 4](step%204.png)

---

### Step 5 - Start Flask App
```bash
# Note: use full path to avoid spaces-in-path issue with $(pwd)
docker run -d \
  --name flask-app \
  --network myapp-network \
  -p 5000:5000 \
  -v "/mnt/d/devops and containerisation/lab/exp5/app:/app" \
  -v app-logs:/var/log/app \
  -e DATABASE_URL="postgresql://postgres:mysecretpassword@postgres:5432/mydatabase" \
  -e REDIS_URL="redis://redis:6379" \
  -e DEBUG="false" \
  -e LOG_LEVEL="INFO" \
  flask-app:latest
```
![step 5](step%205.png)

---

### Step 6 - Verify Setup
```bash
# Check all containers running
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Check all on same network
docker network inspect myapp-network

# Check logs
docker logs postgres
docker logs redis
docker logs flask-app
```
![step 6](step%206.png)

---

### Step 7 - Test Connectivity
```bash
# Test DNS resolution from flask-app
docker exec flask-app python -c "import socket; print(socket.gethostbyname('postgres'))"
docker exec flask-app python -c "import socket; print(socket.gethostbyname('redis'))"

# Test flask endpoint
curl http://localhost:5000/config
```
![step 7](step%207.png)

---

### Issues Faced and Fixes

| Error | Cause | Fix |
|---|---|---|
| `Unable to find image 'and:latest'` | Spaces in path breaking `$(pwd)` | Use full hardcoded path |
| `can't open file '/app/app.py'` | app folder was empty | Copy app.py from flask-app folder |
| `Temporary failure in name resolution` | postgres/redis not on myapp-network or stopped | Start containers and connect to network |
| `endpoint already exists in network` | Container already connected | Skip connect, just start container |
| `container name already in use` | Failed container still exists | `docker rm -f container-name` |
```bash
# Fix — spaces in path
# Wrong
-v $(pwd)/app:/app
# Correct
-v "/mnt/d/devops and containerisation/lab/exp5/app:/app"

# Fix — container name conflict
docker rm -f flask-app

# Fix — connect stopped containers to network
docker start postgres
docker start redis
docker network connect myapp-network postgres
docker network connect myapp-network redis
```

---

### Architecture
```
myapp-network (172.24.0.0/16)
├── postgres  (172.24.0.x) ← volume: postgres-data
├── redis     (172.24.0.x) ← volume: redis-data
└── flask-app (172.24.0.2) ← volume: app, app-logs
        ↓
  host:5000 → curl http://localhost:5000/config
```

---

### Environment Variables Used

| Variable | Value | Purpose |
|---|---|---|
| `POSTGRES_PASSWORD` | mysecretpassword | Database password |
| `POSTGRES_DB` | mydatabase | Database name |
| `DATABASE_URL` | postgresql://...@postgres:5432 | Flask DB connection |
| `REDIS_URL` | redis://redis:6379 | Flask Redis connection |
| `DEBUG` | false | Disable debug mode |
| `LOG_LEVEL` | INFO | Application log level |

---

### Key Lessons
- Always start database containers before app containers
- Use full hardcoded paths when directory names contain spaces
- Custom networks support DNS — containers reach each other by name
- Always verify all containers are on same network before testing connectivity
- `ping` and `nslookup` not available in slim images — use `python -c "import socket"` instead
- Always remove failed containers before reusing name: `docker rm -f container-name`
----
---

# Cleanup Commands

### Stop All Running Containers (keeps data)
```bash
# Stop specific containers
docker stop flask-app postgres redis nginx-custom

# Or stop all at once
docker stop $(docker ps -q)
```

### Start Them Back Up Later
```bash
docker start postgres
docker start redis
docker start flask-app
docker start nginx-custom
```

### Full Cleanup (only when completely done)
```bash
# Stop and remove all containers
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

# Remove all unused volumes
docker volume prune -f

# Remove all unused networks
docker network prune -f

# Remove unused images
docker image prune -f
```

> ⚠️ Only run full cleanup when experiment is completely done — it will delete all containers, volumes and networks permanently.

---

# Key Takeaways

## Volumes
- Data inside containers is lost when container is removed — always use volumes for persistence
- Named volumes are managed by Docker and survive container removal
- Bind mounts link host directories directly to container — changes reflect instantly
- Always use named volumes for databases (postgres, mysql, redis)
- `docker cp` can copy files to/from containers without volumes

## Environment Variables
- Use `-e` flag for single variables, `--env-file` for multiple variables
- `EXPOSE` in Dockerfile is documentation only — always need `-p` to publish ports
- Never hardcode secrets — always use environment variables or env files
- Use `docker exec container env` to verify environment variables inside container

## Monitoring
- `docker stats` shows live CPU, memory, network, disk usage
- `docker logs` shows container output — use `-f` to follow live
- `docker inspect` gives full container configuration details
- `docker events` streams real-time Docker daemon activity
- Always start containers before running `docker stats` — stopped containers show nothing
- Use `--no-stream` in scripts to get one-time snapshot instead of live feed

## Networks
- Default `bridge` network does NOT support DNS by container name — use IP addresses
- Custom networks support DNS — containers reach each other by container name
- Always put related containers on same custom network
- `ping` and `nslookup` not available in slim images — use alpine for network debugging
- Use `docker network inspect` to verify all containers are on correct network

## Multi-Container Setup
- Always start database containers before app containers
- Use full hardcoded paths when directory names contain spaces
- Always verify all containers are on same network before testing connectivity
- Use `docker rm -f container-name` to remove failed containers before reusing name
- `docker ps -a` shows all containers including stopped ones