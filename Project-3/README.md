# 🐳 Django Docker Volume Demo

A sample Django application demonstrating how to **upload files and persist them using Docker volumes**.

---

## 📌 Overview

This project showcases:

* File upload functionality using Django
* Data persistence using Docker volumes
* Running Django app inside a Docker container

---

## 🛠 Tech Stack

* Python
* Django
* Docker

---

## 📂 Project Structure

```bash id="t8v2lp"
django-docker-volume/
├── app/
├── templates/
├── manage.py
├── Dockerfile
└── requirements.txt
```

---

## 🚀 Run Using Docker

### Build Image

```bash id="bnxj3v"
docker build -t django-volume-app .
```

---

### Run Container with Volume

```bash id="o5d3qf"
docker run -d \
  -p 8000:8000 \
  -v django_data:/app/media \
  django-volume-app
```

---

## 🔄 How It Works

* User uploads file via web interface
* Django saves file to `/app/media`
* Docker volume (`django_data`) stores the file
* Data persists even if container is removed

---

## 🌐 Access Application

http://localhost:8000

---

## 🔍 Verify Volume

```bash id="b7a1kv"
docker volume ls
docker volume inspect django_data
```

---

## 🧪 Testing

* Upload a file via UI
* Stop and remove container
* Run container again
* Verify file still exists

---

## 🐳 Future Enhancements

* Use Docker Compose
* Add MySQL/PostgreSQL
* Deploy on AWS EC2
* Add CI/CD pipeline

---

## 👨‍💻 Author

Gaurav Kumbhar
https://github.com/madmaxdevops
