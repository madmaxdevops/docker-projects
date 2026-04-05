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

```bash id="2y7r7s"
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

```bash id="2b5r6q"
.
├── app.py
├── Dockerfile
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Build Docker Image

```bash id="j6l4re"
docker build -t flask-host-demo .
```

---

### 2️⃣ Run with Host Network

```bash id="3c0k1y"
docker run -d --name flask-container --network host flask-host-demo
```

---

## 🌐 Access the Application

Since host networking is used, access directly via:

```id="9x8s1u"
http://<EC2-Public-IP>:<PORT>
```

👉 Example:

```id="q2z6jm"
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

```bash id="c3y2h4"
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
🔗 https://github.com/madmaxdevops

---

