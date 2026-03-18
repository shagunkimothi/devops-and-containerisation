# Part B
# task 1 Single container comparision
# Step 1
```bash
docker run -d \
  --name lab-nginx \
  -p 8081:80 \
  -v "/mnt/d/devops and containerisation/lab/exp6/html:/usr/share/nginx/html" \
  nginx:alpine

  ```
  # Verify
  ```bash
  docker ps
```
# access
``` bash
http://localhost:8081

```
# stop and remove container
```bash
docker stop lab-nginx
docker rm lab-nginx
```
![step 1](step%201.png)
---
# Step 2 
```bash
version: '3.8'

services:
  nginx:
    image: nginx:alpine
    container_name: lab-nginx
    ports:
      - "8081:80"
    volumes:
      - ./html:/usr/share/nginx/html
```
# run
``` bash
docker-compose up -d
```
# verify
```bash
docker compose ps
```
# stop
```bash
docker-compose down
```
![step 2](step%202.png)
---
# Task 2 : Multi container applicstion
# A using docker run
1. Create Network
```bash
docker network create wp-net
```
1. run mysql
```bash
docker run -d \
  --name mysql \
  --network wp-net \
  -e MYSQL_ROOT_PASSWORD=secret \
  -e MYSQL_DATABASE=wordpress \
  mysql:5.7
```
1. Run wordpress
```bash
docker run -d \
  --name wordpress \
  --network wp-net \
  -p 8082:80 \
  -e WORDPRESS_DB_HOST=mysql \
  -e WORDPRESS_DB_PASSWORD=secret \
  wordpress:latest
```
![a](using%20docker%20run.png)

# Part B 
# crete docker-compose.yml
```bash
version: '3.8'

services:
  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: wordpress
    volumes:
      - mysql_data:/var/lib/mysql

  wordpress:
    image: wordpress:latest
    ports:
      - "8082:80"
    environment:
      WORDPRESS_DB_HOST: mysql
      WORDPRESS_DB_PASSWORD: secret
    depends_on:
      - mysql

volumes:
  mysql_data:
```
# run
``` bash
docker compose up -d
```
# stop
``` bash
docker compose down -v
```
![part b](part%20B.png)
---

