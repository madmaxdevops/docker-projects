# 📊 Visitor Counter: Node.js + Redis + Docker

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)

A scalable, containerized web application designed to demonstrate the fundamentals of **Service Orchestration**, **State Management**, and **Microservice Communication**.

---

## 🏗️ Architecture & Workflow

The application follows a classic microservices pattern where the web layer and data layer are decoupled.

**User Request** → **Node.js Server** → **Redis (In-Memory Store)** → **Response**

1.  **Client:** Initiates an HTTP request to the web server.
2.  **Node.js Server:** Processes logic and communicates with Redis.
3.  **Redis:** Maintains a high-speed, persistent visit counter.
4.  **Docker Compose:** Orchestrates the networking between containers.

---

## 🚀 Key Features

* **Lightweight Runtime:** Powered by Node.js 18 (Alpine).
* **High-Speed State:** Uses Redis for atomic counter increments.
* **Infrastructure as Code:** Environment defined via `Dockerfile` and `docker-compose.yml`.
* **Zero Config:** Ready to deploy with a single command.

---

## 📂 Project Structure

```text
.
├── app.js               # Main application logic
├── package.json         # Node.js dependencies
├── Dockerfile           # Node.js container blueprint
├── docker-compose.yml   # Orchestration logic
└── README.md            # Documentation

---

## 👨‍💻 Author

Gaurav Kumbhar
https://github.com/madmaxdevops
