📊 Number of Visits to Site (Node.js + Redis + Docker)
📌 Overview

This project demonstrates a simple and scalable web application that tracks the number of visits to a website using Node.js, Redis, and Docker.

Each time a user accesses the application, the visit counter increments and displays the total number of visits.

🏗️ Architecture

User Request → Node.js Server → Redis → Response (Visit Count)

Node.js handles HTTP requests
Redis stores and updates the visit count
Docker ensures consistent deployment across environments
🚀 Features
Lightweight and fast Node.js server
Persistent visit counter using Redis
Containerized setup with Docker
Easy to scale and deploy
Ideal for learning DevOps fundamentals
📂 Project Structure
app.js – Node.js application
package.json – Dependencies
Dockerfile – Node.js container configuration
docker-compose.yml – Multi-container setup
README.md
⚙️ Prerequisites

Make sure you have installed:

Docker
Docker Compose
🐳 Setup & Run (Using Docker)
Clone the repository
Navigate to the project directory
Run: docker-compose up --build
Open browser and visit: http://localhost:3000

You will see the number of visits displayed on the screen.

🔄 How It Works
User sends a request to the application
Node.js server processes the request
Redis stores and retrieves the visit count
The count is incremented on each visit
Updated count is returned to the user
📈 DevOps Perspective

This project demonstrates:

Containerization using Docker
Service orchestration with Docker Compose
State management using Redis
Microservice communication between services
🔧 Improvements (Future Enhancements)
Add Kubernetes deployment
Implement CI/CD pipeline (Jenkins or GitHub Actions)
Use Nginx as a reverse proxy
Enable persistent Redis storage
Support horizontal scaling
🧪 Testing

You can test the application by refreshing the browser multiple times or by sending repeated requests to the application endpoint.

👨‍💻 Author
Gaurav Kumbhar https://github.com/madmaxdevops
