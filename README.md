# 🏗️ Cement Demand Forecast Forecasting - End-to-End MLOps Project

## 📌 Project Overview

This project demonstrates a complete end-to-end MLOps pipeline for forecasting cement demand using Machine Learning.

The project covers the entire ML lifecycle:

- Data Ingestion
- Data Validation
- Data Transformation
- Feature Engineering
- Model Training
- Model Evaluation
- MLflow Experiment Tracking
- Model Registry
- FastAPI Deployment
- Docker Containerization

The pipeline follows a modular architecture inspired by production MLOps systems.

---

## 🚀 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| ML Library | Scikit-Learn |
| Experiment Tracking | MLflow |
| API | FastAPI |
| Containerization | Docker |
| Configuration | YAML |
| Model Serialization | Joblib |
| Version Control | Git |
| Deployment | Docker |

---

## 📂 Project Structure

```text
cement-demand-forecast-mlops
│
├── artifacts
├── config
├── logs
├── src
│   ├── api
│   ├── components
│   ├── config
│   ├── constants
│   ├── entity
│   ├── pipeline
│   └── utils
│
├── tests
├── Dockerfile
├── requirements.txt
├── main.py
└── README.md
```

---

## 🔄 Project Workflow

```text
Raw Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Train/Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
MLflow Tracking
      │
      ▼
Model Registry
      │
      ▼
FastAPI
      │
      ▼
Docker
```

---

## 📊 ML Pipeline

### Stage 1

Data Ingestion

- Reads raw dataset
- Stores artifacts

### Stage 2

Data Validation

- Checks schema
- Checks required columns
- Generates validation status

### Stage 3

Data Transformation

- Cleans dataset
- Creates features
- Generates train/test data

### Stage 4

Model Training

- Random Forest Regressor
- MLflow Tracking
- Model Registry

### Stage 5

Model Evaluation

Metrics:

- MAE
- RMSE
- R² Score

---

## 📈 MLflow

The project tracks:

- Parameters
- Metrics
- Models
- Model Versions

---

## 🌐 FastAPI

API Endpoint

POST

```
/predict
```

Example

```json
{
  "Production": 350,
  "Sales": 320,
  "population": 125.5,
  "gdp": 180000,
  "disbusment": 65000,
  "interestrate": 10.5
}
```

Example Response

```json
{
    "predicted_demand": 456.77
}
```

---

## 🐳 Docker

Build

```bash
docker build -t cement-demand-api .
```

Run

```bash
docker run -p 8000:8000 cement-demand-api
```

Swagger

```
http://localhost:8000/docs
```

---

## ⚙️ Installation

Clone repository

```bash
git clone https://github.com/<YOUR_USERNAME>/cement-demand-forecast-mlops.git
```

Install

```bash
pip install -r requirements.txt
```

Run Pipeline

```bash
python main.py
```

Run API

```bash
uvicorn src.api.main:app --reload
```

---

## 📊 Model Performance

| Metric | Value |
|---------|--------|
| MAE | XX |
| RMSE | XX |
| R² Score | XX |

---

## 🔮 Future Improvements

- XGBoost
- LightGBM
- CatBoost
- GitHub Actions
- Azure Deployment
- Evidently AI
- Model Monitoring
- Unit Testing
- CI/CD Pipeline

---

## 👨‍💻 Author

Yogesh G

Machine Learning Engineer | Data Scientist | MLOps Engineer

---