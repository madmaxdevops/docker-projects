# 🐳 Django Docker Volume Demo

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Web%20Framework-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Storage](https://img.shields.io/badge/Volumes-Persistent-orange)

A sample Django application demonstrating how to **upload files and persist them using Docker volumes** — a key concept in containerized environments.

---

## 📌 Overview

This project showcases:

* 📤 File upload functionality using Django
* 💾 Persistent storage using Docker volumes
* 🐳 Running Django inside a container
* 🔄 Data retention even after container removal

---

## 🛠 Tech Stack

* **Python 3**
* **Django**
* **Docker**

---

## 📂 Project Structure

```bash
django-docker-volume/
├── app/
├── templates/
├── manage.py
├── Dockerfile
└── requirements.txt
```

---

## 🚀 Run Using Docker

### 1️⃣ Build Image

```bash
docker build -t django-volume-app .
```

### 2️⃣ Run Container with Volume

```bash
docker run -d \
  -p 8000:8000 \
  -v django_data:/app/media \
  django-volume-app
```

---

## 🔄 How It Works

1. User uploads file via web interface
2. Django stores file in `/app/media`
3. Docker volume (`django_data`) stores data
4. Data persists even if container is deleted

---

## 🌐 Access Application

👉 http://localhost:8000

---

## 🔍 Verify Volume

```bash
docker volume ls
docker volume inspect django_data
```

---

## 🧪 Testing Persistence

1. Upload a file via UI
2. Stop & remove container
3. Run container again
4. Verify file still exists ✅

---

## 🚀 Future Enhancements

* 🧩 Use Docker Compose for multi-service setup
* 🗄️ Add PostgreSQL / MySQL database
* ☁️ Deploy on AWS EC2
* 🔄 Add CI/CD pipeline (GitHub Actions / Jenkins)
* 🔐 Add authentication & file validation

---

## 👨‍💻 Author

**Gaurav Kumbhar**
🔗 https://github.com/madmaxdevops

---

## ⭐ Support

If you find this project useful, give it a ⭐ on GitHub!
