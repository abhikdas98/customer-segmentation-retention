🧠 Customer Churn Prediction System — Production-Ready ML Pipeline

An end-to-end Machine Learning system that performs:

📊 Customer Segmentation (RFM + KMeans)

🔍 Churn Prediction (Logistic Regression)

🗄 MongoDB Data Storage

⚡ FastAPI Inference API

🐳 Dockerized Deployment

🌩 AWS EC2 Cloud Hosting

🔁 CI/CD via GitHub Actions

Built with production-grade architecture and MLOps best practices.

🌍 Live Deployment
🚀 Swagger UI
http://13.61.65.27:8000/docs
🩺 Health Check
http://13.61.65.27:8000/health

CI/CD automatically deploys updates on every push to main.

💡 Why This Project Stands Out

Unlike typical ML notebook projects, this system demonstrates:

Production-grade API deployment

Docker multi-container architecture

MongoDB integration

Batch-safe large data ingestion (400K+ records)

Memory tuning for micro cloud instance

CI/CD automation

Model version pinning

Health monitoring endpoint

Real-world debugging in cloud environment

This is a deployment-focused ML system, not just a modeling exercise.

🏗 System Architecture
              GitHub Push
                   ↓
          GitHub Actions (CI/CD)
                   ↓
               AWS EC2
                   ↓
        ┌─────────────────────┐
        │ Docker Compose       │
        │                      │
        │  FastAPI Container   │
        │        ↓             │
        │  Churn Model         │
        │        ↓             │
        │  MongoDB Container   │
        └─────────────────────┘
📂 Project Structure
customer-segmentation-retention/
│
├── app/
│   └── main.py                  # FastAPI application
│
├── src/
│   ├── insert_data.py           # Safe MongoDB batch seeding
│   ├── churn_model.py           # Prediction logic
│   ├── feature_engineering.py   # RFM + behavioral features
│   ├── config.py
│   └── logger.py
│
├── models/
│   ├── logistic_model.pkl
│   └── scaler.pkl
│
├── data/
│   └── raw/online_retail.csv
│
├── .github/workflows/
│   └── deploy.yml               # CI/CD automation
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
📊 Machine Learning Pipeline
1️⃣ Customer Segmentation

RFM feature engineering

Log transformation

KMeans clustering

Silhouette score validation

2️⃣ Churn Modeling

Logistic Regression

Threshold tuning for churn recall optimization

ROC-AUC evaluation

Feature importance interpretation

Data leakage detection & correction

Final production model uses:

Frequency

Monetary

AvgOrderValue

📈 Model Performance
Metric	Score
Accuracy	~74%
ROC-AUC	~0.77
Churn Recall (after tuning)	0.82
📡 Example API Usage
Request
POST /predict_churn_by_id
{
  "customer_id": 12347
}
Response
{
  "customer_id": 12347,
  "features": {
    "Frequency": 7,
    "Monetary": 4310.0,
    "AvgOrderValue": 615.71
  },
  "prediction": {
    "churn_probability": 0.07,
    "churn_prediction": 0
  }
}
🐳 Running Locally with Docker
Build & Start Containers
docker compose build --no-cache
docker compose up
Seed MongoDB (One-time)
docker exec -it churn-api python -m src.insert_data
Access API

Swagger:

http://localhost:8000/docs
🔁 CI/CD Automation

Push to main

GitHub Actions SSH into EC2

Pull latest code

Rebuild Docker containers

Restart API

Fully automated deployment pipeline.

🛠 Production Engineering Challenges Solved
🔹 MongoDB OOM Crash

Fixed WiredTiger cache size for micro instance:

command: ["mongod", "--wiredTigerCacheSizeGB", "0.25"]
🔹 Large Dataset Ingestion

Implemented chunk-based batch insertion to safely seed 400K+ records.

🔹 Docker Networking Issue

Replaced localhost with Docker service name for container communication.

🔹 Version Mismatch

Pinned scikit-learn version to ensure consistent model deserialization.

🔹 Health Monitoring

Implemented /health endpoint for production validation.

🔐 Reproducibility

All dependencies pinned in requirements.txt

Docker ensures consistent runtime

Environment-independent deployment

🚀 Future Improvements

HTTPS with Nginx reverse proxy

Rate limiting

Monitoring & metrics dashboard

Model versioning system

CloudWatch integration

Automated retraining pipeline

👨‍💻 Author

Abhik Das
Data Science | Machine Learning | MLOps