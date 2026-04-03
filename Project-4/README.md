# 🐳 Docker Bridge Network Demo

A sample project demonstrating how **frontend and backend containers communicate using Docker Bridge Network**.

---

## 📌 Overview

This project showcases:

* Running multiple containers (frontend & backend)
* Communication between containers
* Understanding Docker bridge networking

---

## 🛠 Tech Stack

* Docker
* Python / Node (Backend - optional)
* Nginx / Frontend

---

## 📂 Project Structure

```bash id="a9h3sd"
docker-bridge-network/
├── frontend/
├── backend/
├── Dockerfile
└── docker-compose.yml (optional)
```

---

## 🚀 Run Using Docker

### Build Images

```bash id="v1g3ak"
docker build -t frontend-app ./frontend
docker build -t backend-app ./backend
```

---

### Create Bridge Network

```bash id="w38m1h"
docker network create my-bridge-network
```

---

### Run Containers

```bash id="k2c93f"
docker run -d --name backend --network my-bridge-network backend-app
docker run -d --name frontend --network my-bridge-network -p 8080:80 frontend-app
```

---

## 🔄 How It Works

* Both containers are connected to the same bridge network
* Frontend communicates with backend using container name
* Docker provides internal DNS for service discovery

Example:

```bash id="m7qxzw"
http://backend:5000
```

---

## 🌐 Access Application

http://localhost:8080

---

## 🔍 Verify Network

```bash id="g81k9p"
docker network inspect my-bridge-network
```

---

## 🧪 Testing

* Access frontend in browser
* Verify backend responses
* Check container logs

---

## 🐳 Future Enhancements

* Use Docker Compose
* Add reverse proxy (Nginx)
* Deploy on AWS ECS / Kubernetes
* Add CI/CD pipeline

---

## 👨‍💻 Author

Gaurav Kumbhar
https://github.com/madmaxdevops

