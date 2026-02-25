import joblib
import numpy as np
import os
from src.logger import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "logistic_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

# Load model and scaler

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)



def predict_churn(data: dict):

    """
    data = {
        "Frequency": value,
        "Monetary": value,
        "AvgOrderValue": value
    }
    """

    features = np.array([
        data["Frequency"],
        data["Monetary"],
        data["AvgOrderValue"]
    ]).reshape(1, -1)

    features_scaled = scaler.transform(features)

    probability = model.predict_proba(features_scaled)[0][1]

    prediction = int(probability >= 0.35)

    return {
        "churn_probability": float(probability),
        "churn_prediction": prediction
    }
    logger.info("Model loaded successfully.")
