# Docker Storage Practical – Named Volume, Bind Mount & tmpfs

## 🎯 Objective

To demonstrate and compare Docker storage mechanisms:

- Named Volume
- Bind Mount
- tmpfs

Also to verify data persistence and understand common errors.

---

## 🛠 Tools Used

- Docker
- Nginx Image
- MySQL Image
- WSL (Windows Subsystem for Linux)

---

# 🔹 PART 1 – Named Volume

## Step 1: Create Volume

```bash
docker volume create myvolume
```

Verify:

```bash
docker volume ls
```

Inspect volume:

```bash
docker volume inspect myvolume
```

Output shows mount location:

```
/var/lib/docker/volumes/myvolume/_data
```

---

## Step 2: Run Nginx with Named Volume

```bash
docker run -d \
  --name nginx-volume \
  -v myvolume:/usr/share/nginx/html \
  -p 8080:80 \
  nginx
```

---

## Step 3: Create File Inside Container

```bash
docker exec -it nginx-volume bash
```

Inside container:

```bash
echo "<h1>Named Volume Test</h1>" > /usr/share/nginx/html/index.html
exit
```

---

## Result

Open in browser:

```
http://localhost:8080
```

Output:

```
Named Volume Test
```

### ✅ Conclusion

Named volumes:
- Are managed by Docker
- Persist even after container removal
- Stored internally in Docker system

---

# 🔹 PART 2 – Bind Mount

## Step 1: Run Nginx with Bind Mount

```bash
docker run -d \
  --name nginx-bind \
  -v /home/shagunkimothi/html:/usr/share/nginx/html \
  -p 8081:80 \
  nginx
```

---

## Step 2: Permission Issue Encountered

Error:

```
Permission denied
```

Check ownership:

```bash
ls -ld /home/shagunkimothi/html
```

Output:

```
drwxr-xr-x 2 root root ...
```

Reason:
Folder owned by root → normal user cannot write.

---

## Step 3: Fix Permission

```bash
sudo chown -R shagunkimothi:shagunkimothi /home/shagunkimothi/html
```

Verify:

```bash
ls -ld /home/shagunkimothi/html
```

Now owned by:

```
shagunkimothi shagunkimothi
```

---

## Step 4: Create File on Host

```bash
echo "<h1>Bind Mount Test</h1>" > /home/shagunkimothi/html/index.html
```

---

## Result

Open in browser:

```
http://localhost:8081
```

Output:

```
Bind Mount Test
```

### ✅ Conclusion

Bind mounts:
- Use real host directories
- Changes on host reflect immediately in container
- Subject to Linux file permissions
- Best for development

---

# 🔹 PART 3 – tmpfs Mount

## Step 1: Run Nginx with tmpfs

```bash
docker run -d \
  --name nginx-tmpfs \
  --mount type=tmpfs,target=/usr/share/nginx/html \
  -p 8082:80 \
  nginx
```

---

## Step 2: Create File Inside tmpfs

```bash
docker exec -it nginx-tmpfs bash
```

Inside container:

```bash
echo "<h1>TMPFS Test</h1>" > /usr/share/nginx/html/index.html
exit
```

---

## Result

Open in browser:

```
http://localhost:8082
```

Output:

```
TMPFS Test
```

---

## Step 3: Test Persistence

Stop container:

```bash
docker stop nginx-tmpfs
```

Start again:

```bash
docker start nginx-tmpfs
```

Refresh browser.

Result:
Default Nginx page appears.

### ❌ File disappeared

---

### ✅ Conclusion

tmpfs:
- Stored in RAM
- Data lost when container stops
- Used for cache or temporary data
- Not persistent

---

# 🔹 PART 4 – MySQL with Named Volume

```bash
docker run -d \
  --name mysql-container \
  --mount source=myvolume,target=/var/lib/mysql \
  mysql
```

Purpose:
Demonstrates database persistence using named volumes.

---

# 🔥 Common Errors and Reasons

### 1. unknown flag: --it
Reason:
Correct flag is `-it`, not `--it`.

---

### 2. bind source path does not exist
Reason:
Host folder must exist before mounting.

---

### 3. Permission denied
Reason:
Folder owned by root.
Solved using `chown`.

---

### 4. Container name conflict
Reason:
Container already exists.
Solved using:

```bash
docker rm -f container_name
```

---

# 📊 Final Comparison

| Feature | Named Volume | Bind Mount | tmpfs |
|----------|--------------|------------|--------|
| Stored In | Docker system | Host filesystem | RAM |
| Persistent | ✅ Yes | ✅ Yes | ❌ No |
| Visible on Host | ❌ No | ✅ Yes | ❌ No |
| Best For | Databases | Development | Cache/Temp Data |

---

# 🏁 Final Conclusion

This practical successfully demonstrated:

✔ Named volume persistence  
✔ Bind mount host integration  
✔ tmpfs temporary storage behavior  
✔ Linux permission handling  
✔ Container lifecycle management  

Docker provides flexible storage options depending on persistence, performance, and development needs.
