# 🐳 Docker Bridge Network Demo

A sample project demonstrating how **frontend and backend containers communicate** using Docker Bridge Network.

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

```bash
docker-bridge-network/
├── frontend/
├── backend/
├── Dockerfile
└── docker-compose.yml (optional)
```

---

## 🚀 Run Using Docker

### 1️⃣ Build Images

```bash
docker build -t frontend-app ./frontend
docker build -t backend-app ./backend
```

---

### 2️⃣ Create Bridge Network

```bash
docker network create my-bridge-network
```

---

### 3️⃣ Run Containers

```bash
docker run -d --name backend --network my-bridge-network backend-app
docker run -d --name frontend --network my-bridge-network -p 8080:80 frontend-app
```

---

## 🔄 How It Works

* Both containers are connected to the same **bridge network**
* Frontend communicates with backend using **container name**
* Docker provides **internal DNS for service discovery**

### ✅ Example

```bash
http://backend:5000
```

---

## 🌐 Access Application

```bash
http://localhost:8080
```

---

## 🔍 Verify Network

```bash
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

**Gaurav Kumbhar**
🔗 https://github.com/madmaxdevops

---
