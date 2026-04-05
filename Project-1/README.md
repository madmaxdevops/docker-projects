# 🚀 Visitor Counter — Node.js + Redis + Docker

<p align="center">
  <img src="https://img.shields.io/badge/Node.js-18--Alpine-339933?style=for-the-badge&logo=node.js&logoColor=white" alt="Node.js"/>
  <img src="https://img.shields.io/badge/Redis-In--Memory_Store-DC382D?style=for-the-badge&logo=redis&logoColor=white" alt="Redis"/>
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Docker_Compose-Orchestrated-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Compose"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License"/>
</p>

<p align="center">
  A scalable, containerized web application demonstrating <strong>Service Orchestration</strong>, <strong>State Management</strong>, and <strong>Microservice Communication</strong> — all with a single command.
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Architecture and Workflow](#️-architecture-and-workflow)
- [Key Features](#-key-features)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Getting Started](#-getting-started)
- [API Reference](#-api-reference)
- [Environment Variables](#-environment-variables)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 🌟 Overview

The **Visitor Counter** is a lightweight, production-ready microservices demo built with **Node.js**, **Redis**, and **Docker Compose**. Every time a user visits the endpoint, the server atomically increments a Redis counter and returns the current visit count — showcasing how decoupled services communicate in a containerized environment.

---

## 🏗️ Architecture and Workflow

```
Client (HTTP Request)
        │
        ▼
 ┌─────────────────┐
 │  Node.js Server  │  ← Business Logic Layer
 │   (Port 3000)    │
 └────────┬────────┘
          │  INCR / GET
          ▼
 ┌─────────────────┐
 │      Redis       │  ← State / Persistence Layer
 │  (In-Memory DB)  │
 └─────────────────┘
          │
          ▼
   JSON Response
{ visits: N, message: "..." }
```

| Step | Actor | Responsibility |
|------|-------|----------------|
| 1 | **Client** | Sends an HTTP `GET /` request |
| 2 | **Node.js** | Connects to Redis and fires `INCR visits` |
| 3 | **Redis** | Atomically increments the counter and returns the value |
| 4 | **Node.js** | Formats and sends the JSON response |
| 5 | **Docker Compose** | Manages networking, volumes, and service dependencies |

---

## 🚀 Key Features

- ⚡ **Lightweight Runtime** — Powered by Node.js 18 (Alpine), keeping the image footprint minimal
- 🔴 **High-Speed State** — Redis atomic `INCR` operations guarantee thread-safe counter updates
- 🐳 **Infrastructure as Code** — Full environment defined via `Dockerfile` and `docker-compose.yml`
- 🔌 **Zero Configuration** — Deploy instantly with a single `docker compose up` command
- 🌐 **REST-Ready** — Clean HTTP API with JSON responses
- 🔁 **Auto-Restart Policy** — Services restart automatically on failure

---

## 📂 Project Structure

```
visitor-counter/
├── app.js                # Main application logic & Redis client
├── package.json          # Node.js dependencies & scripts
├── Dockerfile            # Node.js container blueprint (Alpine)
├── docker-compose.yml    # Multi-service orchestration config
└── README.md             # Project documentation
```

---

## 🔧 Prerequisites

Make sure you have the following installed:

| Tool | Version | Purpose |
|------|---------|---------|
| [Docker](https://docs.docker.com/get-docker/) | 20.x+ | Container runtime |
| [Docker Compose](https://docs.docker.com/compose/) | 2.x+ | Service orchestration |

> **Note:** No local Node.js or Redis installation required — everything runs inside containers.

---

## ⚡ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/madmaxdevops/visitor-counter.git
cd visitor-counter
```

### 2. Start the Application

```bash
docker compose up --build
```

### 3. Visit the App

Open your browser or use `curl`:

```bash
curl http://localhost:3000
```

**Sample Response:**

```json
{
  "visits": 42,
  "message": "Welcome! You are visitor number 42."
}
```

### 4. Stop the Application

```bash
docker compose down
```

To also remove volumes (reset the counter):

```bash
docker compose down -v
```

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Returns current visit count and welcome message |
| `GET` | `/health` | Health check — confirms Node.js & Redis connectivity |
| `DELETE` | `/reset` | Resets the visitor counter to `0` |

---

## 🌍 Environment Variables

Configure the app using environment variables in `docker-compose.yml` or a `.env` file:

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `3000` | Port the Node.js server listens on |
| `REDIS_HOST` | `redis` | Redis service hostname |
| `REDIS_PORT` | `6379` | Redis port |

---

## 🔭 Future Enhancements

### 🛡️ Security & Auth
- [ ] Add API key / JWT authentication middleware
- [ ] Implement rate limiting per IP using Redis TTL
- [ ] Add HTTPS support via Nginx reverse proxy with SSL termination

### 📊 Observability & Monitoring
- [ ] Integrate **Prometheus** metrics endpoint (`/metrics`)
- [ ] Add **Grafana** dashboard for real-time visit analytics
- [ ] Centralized logging with **Winston** + **ELK Stack** (Elasticsearch, Logstash, Kibana)
- [ ] Distributed tracing with **OpenTelemetry**

### 🚀 Scalability
- [ ] Add **Redis Cluster** support for horizontal scaling
- [ ] Introduce **Nginx** load balancer to scale Node.js horizontally (`--scale web=3`)
- [ ] Migrate to **Kubernetes** with a Helm chart for production-grade orchestration
- [ ] Implement **Redis Sentinel** for high availability failover

### 🗄️ Data & Persistence
- [ ] Persist visit history to **PostgreSQL** or **MongoDB**
- [ ] Add per-route and per-user visit tracking
- [ ] Introduce a time-series dashboard (visits/hour, visits/day)
- [ ] Export analytics to CSV / PDF via a REST endpoint

### 🧪 Testing & CI/CD
- [ ] Unit tests with **Jest** + integration tests with **Supertest**
- [ ] GitHub Actions CI/CD pipeline (lint → test → build → push to Docker Hub)
- [ ] Docker image scanning with **Trivy** or **Snyk**
- [ ] Auto-deploy to **AWS ECS** / **Google Cloud Run** on merge to `main`

### 🎨 Developer Experience
- [ ] Add a live **web dashboard** (React / Vue) to display visit stats visually
- [ ] Hot-reload in development using **nodemon**
- [ ] Multi-environment support (`dev`, `staging`, `prod`) via Docker Compose overrides
- [ ] OpenAPI / Swagger documentation at `/docs`

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'feat: add your feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages.

---

## 👨‍💻 Author

<div align="center">

[![GitHub followers](https://img.shields.io/github/followers/madmaxdevops?label=Follow%20%40madmaxdevops&style=social)](https://github.com/madmaxdevops)

**Gaurav Kumbhar**

[![GitHub](https://img.shields.io/badge/GitHub-madmaxdevops-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/madmaxdevops)

*Built with ❤️ and lots of ☕ — feel free to reach out via GitHub for collaborations or questions!*

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details. 

---

<p align="center">
  ⭐ Found this project helpful? Give it a star on GitHub — it means a lot!
</p>

