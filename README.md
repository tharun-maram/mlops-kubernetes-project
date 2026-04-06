# 🚀 End-to-End MLOps Pipeline using Kubernetes, Docker & MLflow

## 📌 Project Overview

This project demonstrates a complete **MLOps (Machine Learning Operations) pipeline** where a machine learning model is trained, tracked, containerized, deployed, and served as an API using modern cloud-native tools.

Unlike traditional ML projects that stop at training, this system covers the **full lifecycle of machine learning in production**.

---

## 🎯 Key Features

* ✅ Train ML model using Kubernetes Jobs
* 📊 Track experiments using MLflow
* 🐳 Containerize applications using Docker
* ☸️ Deploy services using Kubernetes
* 🌐 Serve predictions via REST API (Flask)
* 🚀 End-to-end automated ML pipeline

---

## 🧠 Architecture / Workflow

User Input → API (Flask) → Model Prediction
↑
Kubernetes Deployment (API)
↑
Docker Image
↑
MLflow Tracking ← Kubernetes Job (Training)

---

## ⚙️ Tech Stack

| Category            | Tools        |
| ------------------- | ------------ |
| Programming         | Python       |
| ML Framework        | Scikit-learn |
| Containerization    | Docker       |
| Orchestration       | Kubernetes   |
| Experiment Tracking | MLflow       |
| API                 | Flask        |
| Cloud               | AWS EC2      |

---

## 📂 Project Structure

ml-project/
├── train.py            # Model training script
├── app.py              # Flask API for predictions
├── Dockerfile          # Docker image configuration
├── requirements.txt    # Dependencies
├── ml-job.yaml         # Kubernetes Job (training)
├── ml-api.yaml         # Kubernetes Deployment + Service
└── README.md           # Project documentation

---

## 🔄 How It Works (Step-by-Step)

### 1️⃣ Model Training

* A machine learning model is trained using `train.py`
* The training runs as a **Kubernetes Job**
* MLflow logs:

  * Parameters
  * Metrics
  * Experiment details

---

### 2️⃣ Experiment Tracking

* MLflow UI displays:

  * Runs
  * Metrics
  * Performance comparison

---

### 3️⃣ Containerization

* The project is packaged into a Docker image
* Ensures consistent environment across systems

---

### 4️⃣ Deployment

* Kubernetes Deployment runs the API continuously
* Service exposes the API to external users

---

### 5️⃣ Prediction API

* Flask API receives input
* Returns prediction in real-time

Example:

POST /predict
{
"value": 5
}

Response:
{
"prediction": 10
}

---

## 🚀 How to Run This Project (For New Users)

### 🔹 Prerequisites

* Docker installed
* Kubernetes cluster (Minikube / Kubeadm / Cloud)
* Python 3.x
* Git

---

### 🔹 Step 1: Clone Repository

git clone https://github.com/tharun-maram/mlops-kubernetes-project.git
cd mlops-kubernetes-project

---

### 🔹 Step 2: Build Docker Image

docker build -t your-dockerhub-username/ml-project .

---

### 🔹 Step 3: Push to Docker Hub

docker push your-dockerhub-username/ml-project

---

### 🔹 Step 4: Run Training Job

kubectl apply -f ml-job.yaml

---

### 🔹 Step 5: Deploy API

kubectl apply -f ml-api.yaml

---

### 🔹 Step 6: Access API

kubectl port-forward svc/ml-api-service 5001:5001

Then open:
http://localhost:5001

---

### 🔹 Step 7: Test Prediction

curl -X POST http://localhost:5001/predict 
-H "Content-Type: application/json" 
-d '{"value": 5}'

---

## 📊 MLflow Setup

Run MLflow UI:

mlflow ui --host 0.0.0.0 --port 5000

Access:
http://localhost:5000

---

## 🏆 Key Learning Outcomes

* End-to-end MLOps pipeline design
* Kubernetes-based ML job execution
* Experiment tracking with MLflow
* Docker-based containerization
* API deployment and real-time inference

---

## 🔥 Why This Project is Important

Most ML projects only focus on training models.
This project demonstrates **production-level ML system design**, including:

* Scalability
* Automation
* Deployment
* Monitoring

---

## 👨‍💻 Author

**Tharun Maram**
GitHub: https://github.com/tharun-maram

---

## ⭐ Future Improvements

* Use real datasets (e.g., housing data)
* Store models in S3
* Add frontend UI
* Implement CI/CD pipeline
* Load trained model in API

---

## 💡 Final Note

This project represents a **real-world MLOps workflow**, similar to how machine learning systems are built and deployed in industry.
