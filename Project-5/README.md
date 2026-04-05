# 🐳 Docker Host Network Demo

This repository demonstrates how **Docker Host Network mode** works using a simple Python Flask application.

---

## 📌 Overview

This project contains a minimal Flask app that prints a **Hello message**, used to understand:

* How Docker networking works
* Difference between **bridge network** and **host network**
* Why port mapping is not required in host mode

---

## 🧠 Key Concept

When running a container with:

```bash
docker run --network host <image>
```

👉 The container shares the **host machine’s network**

* No separate IP
* No port mapping (`-p`)
* Application runs directly on host ports

---

## 🛠 Tech Stack

* Python
* Flask
* Docker

---

## 📂 Project Structure

```bash
.
├── app.py
├── Dockerfile
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Build Docker Image

```bash
docker build -t flask-host-demo .
```

---

### 2️⃣ Run with Host Network

```bash
docker run -d --name flask-container --network host flask-host-demo
```

---

## 🌐 Access the Application

Since host networking is used, access directly via:

```
http://<EC2-Public-IP>:<PORT>
```

👉 Example:

```
http://<EC2-IP>:6100
```

---

## 🔍 Important Observation

* The port defined inside `app.py` is directly exposed on the host
* Dockerfile `EXPOSE` instruction is ignored in host mode
* No `-p` (port mapping) is required

---

## ⚠️ Limitations of Host Network

* ❌ No network isolation
* ❌ Port conflicts if multiple containers use same port
* ❌ Not recommended for production use

---

## ✅ Best Practice

For production environments, use:

```bash
docker run -p 6100:6100 flask-host-demo
```

✔️ Provides isolation
✔️ Better security
✔️ Scalable architecture

---

## 🎯 Learning Outcome

After this demo, you will understand:

* How Docker host networking works
* Why applications are directly accessible on host ports
* Difference between **host vs bridge networking**

---

## 👨‍💻 Author

**Gaurav Kumbhar**
📧 [gauravkumbhar9987@gmail.com](mailto:gauravkumbhar9987@gmail.com)

---

