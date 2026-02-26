from fastapi import FastAPI
from pydantic import BaseModel
from src.churn_model import predict_churn
from src.feature_engineering import get_customer_transactions, compute_features
from src.insert_data import seed_data
from src.logger import logger
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts customer churn probability",
    version="1.0"
)


class CustomerData(BaseModel):
    Frequency: float
    Monetary: float
    AvgOrderValue: float

class CustomerIDInput(BaseModel):
    customer_id: int

@app.on_event("startup")
def startup_event():
    logger.info("API starting...")


@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}


@app.post("/predict_churn")
def churn_prediction(customer: CustomerData):
    result = predict_churn(customer.dict())
    return result

@app.post("/predict_churn_by_id")
def churn_by_customer_id(customer: CustomerIDInput):

    df = get_customer_transactions(customer.customer_id)

    if df is None:
        return {"error": "Customer not found"}

    features = compute_features(df)

    result = predict_churn(features)

    return {
        "customer_id": customer.customer_id,
        "features": features,
        "prediction": result
    }


@app.get("/health")
def health_check():
    mongo_status = "not connected"

    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
        client.admin.command("ping")   # Proper Mongo health check
        mongo_status = "connected"
    except PyMongoError:
        mongo_status = "not connected"

    return {
        "api": "running",
        "mongo": mongo_status,
        "model": "loaded"
    }
    logger.error("Mongo connection failed.")