# Docker Volume Practical – Named Volume Demonstration

## 🎯 Objective

To demonstrate Docker named volumes, verify data persistence across containers,
and understand common Docker command errors with proper reasoning.

---

## 🛠 Tools Used

- Docker
- Ubuntu Image
- WSL (Windows Subsystem for Linux)
- Windows OS

---

# PART 1 – Creating a Named Volume

## Step 1: Create Volume

```bash
docker volume create myvolume
```

### Explanation:
This command creates a Docker named volume called `myvolume`.

Docker stores named volumes internally at:
```
/var/lib/docker/volumes/
```

These volumes are managed by Docker, not by the current working directory.

---

## Step 2: Verify Volume

```bash
docker volume ls
```

This confirms that the volume has been successfully created.

---

# PART 2 – Mount Volume to Container

## Step 3: Run Container with Volume

```bash
docker run -it --name myvolume \
-v myvolume:/home/app \
ubuntu /bin/bash
```

### Explanation of Command:

- `-it` → Runs container in interactive terminal mode  
- `--name myvolume` → Assigns container name  
- `-v myvolume:/home/app` → Mounts named volume inside container  
- `ubuntu` → Image name  
- `/bin/bash` → Command executed inside container  

---

## Step 4: Create File Inside Volume

Inside container:

```bash
cd /home/app
echo "sapid500120283" > sapid.txt
ls
```

This creates a file inside the mounted volume.

---

## Step 5: Exit Container

```bash
exit
```

The container stops but the volume remains intact.

---

# PART 3 – Verify Data Persistence

## Step 6: Remove Container

```bash
docker rm myvolume
```

Important:
Removing a container does NOT remove its named volume.

---

## Step 7: Reattach Volume to New Container

```bash
docker run -it --rm \
-v myvolume:/data \
ubuntu /bin/bash
```

Inside container:

```bash
ls /data
```

Output:

```
sapid.txt
```

### Result:
The file still exists, proving that Docker named volumes persist data
even after container removal.

---

# Common Errors and Reasons

---

## ❌ Error 1: Using `--it` Instead of `-it`

Incorrect:

```bash
docker run --it ...
```

Error:
```
unknown flag: --it
```

### Reason:
Docker uses short flags `-i` and `-t`.
There is no `--it` flag.

Correct:

```bash
docker run -it ...
```

---

## ❌ Error 2: Missing Image Name

Incorrect:

```bash
docker run -it -v myvolume:/home/app
```

Error:
```
docker run requires at least 1 argument
```

### Reason:
Docker run syntax requires an IMAGE.

Correct structure:

```
docker run [OPTIONS] IMAGE [COMMAND]
```

Correct example:

```bash
docker run -it -v myvolume:/home/app ubuntu /bin/bash
```

---

## ❌ Error 3: Using `ubuntu/bin/bash` as Image

Incorrect:

```bash
docker run -it ubuntu/bin/bash
```

Error:
```
pull access denied for ubuntu/bin/bash
```

### Reason:
Docker interprets `ubuntu/bin/bash` as an image name.

Correct:

```bash
docker run -it ubuntu /bin/bash
```

Image and command must be separated by a space.

---

## ❌ Error 4: Container Name Conflict

Error:
```
container name is already in use
```

### Reason:
Container was stopped but not removed.
Docker does not allow duplicate container names.

Solutions:

```bash
docker rm container_name
```

or

```bash
docker start -ai container_name
```

---

## ❌ Error 5: Trying to Access Named Volume as Folder

Incorrect:

```bash
cd myvolume
```

Error:
```
No such file or directory
```

### Reason:
Named volumes are not stored in the current directory.
They are managed internally by Docker.

Correct method:
Mount the volume into a container to access it.

---

# Key Concepts Learned

- Docker named volumes persist data
- Volumes are independent of container lifecycle
- Removing a container does NOT remove its volume
- Correct Docker run syntax
- Difference between image and command
- Container naming conflicts
- Named volume vs bind mount

---

# Conclusion

This practical successfully demonstrated:

✔ Creation of Docker named volume  
✔ Mounting volume to container  
✔ Data persistence across container deletion  
✔ Understanding and resolving common Docker errors  

Docker named volumes provide reliable persistent storage
that survives container removal and can be reused across multiple containers.
