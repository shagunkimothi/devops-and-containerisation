# 🐳 Docker Daemon & Socket Exploration — 4 February 2026

> Exploring Docker internals: version info, Unix socket, TCP socket, daemon configuration, and troubleshooting.

---

## Commands Covered

### 1. Check Docker Version

```bash
docker version
```

**Output:**
```
Client:
  Version:           28.2.2
  API version:       1.50
  Go version:        go1.23.1
  Git commit:        28.2.2-0ubuntu1~24.04.1
  Built:             Wed Sep 10 14:16:39 2025
  OS/Arch:           linux/amd64
  Context:           default

Server:
  Engine:
    Version:         28.2.2
    API version:     1.50 (minimum version 1.24)
    Go version:      go1.23.1
    Git commit:      28.2.2-0ubuntu1~24.04.1
    Built:           Wed Sep 10 14:16:39 2025
    OS/Arch:         linux/amd64
    Experimental:    false
  containerd:
    Version:         1.7.28
  runc:
    Version:         1.3.3-0ubuntu1~24.04.3
  docker-init:
    Version:         0.19.0
```

---

### 2. Docker Info

```bash
docker info
```

Shows detailed system-wide information including client version, context, and debug mode.

---

### 3. Inspect Docker Unix Socket

```bash
ls -l /var/run/docker.sock
```

**Output:**
```
srw-rw---- 1 root docker 0 Feb 4 05:48 /var/run/docker.sock
```

> The Docker daemon listens on a Unix socket at `/var/run/docker.sock` by default.

---

### 4. Query Docker via Unix Socket using curl

```bash
curl --unix-socket /var/run/docker.sock http://localhost/version
```

Returns a JSON response with Docker engine version, API version, OS, architecture, and kernel info — directly from the daemon via the socket.

---

### 5. Edit Daemon Configuration

```bash
sudo nano /etc/docker/daemon.json
```

Used to configure Docker daemon settings such as enabling TCP socket, setting log drivers, etc.

---

### 6. Check Listening Ports (no TCP socket yet)

```bash
ss -lntp | grep 2375
ss -lntp
```

**Output (before enabling TCP):**

| State  | Recv-Q | Send-Q | Local Address:Port   | Peer Address:Port |
|--------|--------|--------|----------------------|-------------------|
| LISTEN | 0      | 4096   | 127.0.0.53%lo:53     | 0.0.0.0:*         |
| LISTEN | 0      | 4096   | 127.0.0.1:33747      | 0.0.0.0:*         |
| LISTEN | 0      | 1000   | 10.255.255.254:53    | 0.0.0.0:*         |
| LISTEN | 0      | 4096   | 127.0.0.54:53        | 0.0.0.0:*         |

> Port `2375` was **not listening** — Docker TCP socket was not yet enabled.

---

### 7. Docker Service Troubleshooting

After editing `daemon.json`, the Docker service failed to start:

```bash
sudo service docker status
```

**Error observed:**
```
Active: failed (Result: exit-code)
docker.service: Start request repeated too quickly.
docker.service: Failed with result 'exit-code'.
Failed to start docker.service - Docker Application Container Engine.
```

**Steps attempted:**
```bash
sudo service docker stop
sudo service docker start
sudo service docker status
```

> The daemon kept failing due to a misconfiguration in `daemon.json`. This is a common issue when the JSON syntax is incorrect or an unsupported option is used.

---

### 8. Enable TCP Socket & Verify

After fixing `daemon.json` to expose the TCP socket on port `2375`:

```bash
ss -lntp | grep 2375
```

**Output:**
```
LISTEN 0  4096  *:2375  *:*
```

> Port `2375` is now listening — Docker daemon is accessible over TCP (unauthenticated, use only on trusted networks).

---

### 9. Query Docker via TCP using curl

```bash
curl http://localhost:2375/version
```

Returns the same JSON version info as the Unix socket method, but over TCP.

---

## Key Concepts Learned

| Concept | Detail |
|---|---|
| Docker Unix Socket | `/var/run/docker.sock` — default IPC between Docker CLI and daemon |
| Docker TCP Socket | Port `2375` (unencrypted) / `2376` (TLS) for remote API access |
| `daemon.json` | Configuration file for Docker daemon at `/etc/docker/daemon.json` |
| `ss -lntp` | Lists all TCP listening ports and associated processes |
| `curl` + socket | Can query Docker REST API directly without CLI |
| Service failure | Misconfigured `daemon.json` causes daemon to crash on start |

---

## Observations

- Docker exposes a full REST API accessible via both Unix socket and TCP.
- The Unix socket is more secure (requires `docker` group membership).
- TCP on port `2375` is **unauthenticated** — never expose on public networks.
- Always validate `daemon.json` syntax before restarting the daemon:
  ```bash
  sudo dockerd --validate
  ```