# 🐳 Microservices Voting App (Docker on AWS EC2)

A simple **microservices-based voting application** deployed using Docker on AWS EC2. This project demonstrates containerization, service communication, and real-world DevOps practices.

---

## 📌 Project Overview

This application allows users to vote between two options (e.g., Cats 🐱 vs Dogs 🐶).
It uses multiple containers that communicate with each other.

---

## 🏗️ Architecture

* **Vote App (Frontend)** → Collects user votes
* **Redis** → Temporary data store (queue)
* **Worker App** → Processes votes
* **PostgreSQL** → Stores results permanently
* **Result App** → Displays voting results

---

## 🔄 Data Flow

1. User submits vote via Vote App
2. Vote stored in Redis
3. Worker reads from Redis
4. Worker writes to PostgreSQL
5. Result App fetches results from DB
6. User views results

---

## 🚀 Setup & Installation (EC2)

### 1️⃣ Install Docker

```bash
sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user
```

---

### 2️⃣ Clone Repository

```bash
git clone https://github.com/raghuck/microservices-example-voting-app.git
cd microservices-example-voting-app
```

---

## ▶️ Run Application (Step-by-Step)

### 🔹 Start Redis

```bash
docker run -d --name redis redis
```

### 🔹 Start Voting App

```bash
docker run -d -p 5000:80 --link redis:redis dockersamples/examplevotingapp_vote
```

### 🔹 Start PostgreSQL

```bash
docker run -d --name=db -e POSTGRES_PASSWORD=postgres postgres:9.4
```

### 🔹 Build & Run Worker

```bash
cd worker
docker build -t worker-app .
docker run -d --link redis:redis --link db:db worker-app
```

### 🔹 Build & Run Result App

```bash
cd ../result
docker build -t result-app .
docker run -d -p 7000:80 --link db:db result-app
```

---

## 🌐 Access Application

* Vote App 👉 http://<EC2-PUBLIC-IP>:5000
* Result App 👉 http://<EC2-PUBLIC-IP>:7000

---

## ⚠️ Issues Faced

* Docker permission denied
* Image not found
* Container dependency issues
* Typo errors in commands
* Deprecated `--link` usage

👉 See `ISSUE.md` for detailed troubleshooting.

---

## 💡 Improvements (Future Scope)

* Use **Docker Compose** (single command setup)
* Replace `--link` with Docker networks
* Add CI/CD pipeline (GitHub Actions)
* Deploy on Kubernetes
* Add monitoring (Prometheus + Grafana)

---

## 🛠️ Tech Stack

* Docker
* AWS EC2
* Redis
* PostgreSQL
* Node.js
* .NET

---

## 👨‍💻 Author

**Gaurav Kumbhar**
DevOps Engineer | AWS | Docker | Automation
🔗 GitHub: https://github.com/gauravkumbhar9987

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
