# 🚀 Visitor Counter — Node.js + Redis + Docker

![Node.js](https://img.shields.io/badge/Node.js-18-green)
![Redis](https://img.shields.io/badge/Redis-7-red)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Docker Compose](https://img.shields.io/badge/Compose-Orchestration-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

A scalable, containerized web application demonstrating **Service Orchestration, State Management, and Microservice Communication** — all with a single command.

---

## 📋 Table of Contents

* [Overview](#-overview)
* [Architecture and Workflow](#-architecture-and-workflow)
* [Key Features](#-key-features)
* [Project Structure](#-project-structure)
* [Prerequisites](#-prerequisites)
* [Getting Started](#-getting-started)
* [API Reference](#-api-reference)
* [Environment Variables](#-environment-variables)
* [Future Enhancements](#-future-enhancements)
* [Contributing](#-contributing)
* [Author](#-author)
* [License](#-license)

---

## 🌟 Overview

The **Visitor Counter** is a lightweight, production-ready microservices demo built with **Node.js, Redis, and Docker Compose**.

Every time a user visits the endpoint:

* The server increments a Redis counter
* Returns the current visit count

👉 Demonstrates **decoupled service communication in containers**

---

## 🏗️ Architecture and Workflow

```
Client (HTTP Request)
        │
        ▼
 ┌─────────────────┐
 │  Node.js Server │  ← Business Logic Layer
 │   (Port 3000)   │
 └────────┬────────┘
          │  INCR / GET
          ▼
 ┌─────────────────┐
 │      Redis      │  ← State Layer
 │  (In-Memory DB) │
 └─────────────────┘
          │
          ▼
   JSON Response
{ visits: N, message: "..." }
```

### 🔄 Flow

| Step | Actor   | Responsibility       |
| ---- | ------- | -------------------- |
| 1    | Client  | Sends HTTP request   |
| 2    | Node.js | Calls Redis (`INCR`) |
| 3    | Redis   | Updates counter      |
| 4    | Node.js | Returns JSON         |
| 5    | Docker  | Manages services     |

---

## 🚀 Key Features

* ⚡ Lightweight Node.js (Alpine)
* 🔴 Redis atomic counter (`INCR`)
* 🐳 Dockerized microservices
* 🔌 One-command setup
* 🌐 REST API ready
* 🔁 Auto-restart containers

---

## 📂 Project Structure

```
visitor-counter/
├── app.js
├── package.json
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🔧 Prerequisites

| Tool           | Version |
| -------------- | ------- |
| Docker         | 20.x+   |
| Docker Compose | 2.x+    |

👉 No need to install Node.js or Redis locally

---

## ⚡ Getting Started

### 1️⃣ Clone Repo

```bash
git clone https://github.com/madmaxdevops/visitor-counter.git
cd visitor-counter
```

### 2️⃣ Run App

```bash
docker compose up --build
```

### 3️⃣ Access App

```bash
curl http://localhost:3000
```

### ✅ Sample Output

```json
{
  "visits": 42,
  "message": "Welcome! You are visitor number 42."
}
```

### 4️⃣ Stop App

```bash
docker compose down
```

### 🔄 Reset Counter

```bash
docker compose down -v
```

---

## 📡 API Reference

| Method | Endpoint | Description     |
| ------ | -------- | --------------- |
| GET    | /        | Get visit count |
| GET    | /health  | Health check    |
| DELETE | /reset   | Reset counter   |

---

## 🌍 Environment Variables

| Variable   | Default | Description    |
| ---------- | ------- | -------------- |
| PORT       | 3000    | App port       |
| REDIS_HOST | redis   | Redis hostname |
| REDIS_PORT | 6379    | Redis port     |

---

## 🔭 Future Enhancements

### 🛡️ Security

* JWT Authentication
* Rate Limiting
* HTTPS (Nginx)

### 📊 Monitoring

* Prometheus + Grafana
* ELK Stack logging
* OpenTelemetry tracing

### 🚀 Scalability

* Redis Cluster
* Load Balancer (Nginx)
* Kubernetes deployment

### 🗄️ Data

* PostgreSQL / MongoDB
* Analytics dashboard

### 🧪 CI/CD

* GitHub Actions
* Docker image scanning
* Auto deploy (AWS/GCP)

---

## 🤝 Contributing

```bash
git checkout -b feature/your-feature
git commit -m "feat: add feature"
git push origin feature/your-feature
```

Then create a Pull Request 🚀

---

## 👨‍💻 Author

**Gaurav Kumbhar**
🔗 https://github.com/madmaxdevops

Built with ❤️ and ☕

---

## 📄 License

This project is licensed under the **MIT License**


---

<p align="center">
  ⭐ Found this project helpful? Give it a star on GitHub — it means a lot!
</p>

