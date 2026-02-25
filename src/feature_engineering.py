from pymongo import MongoClient
import pandas as pd
import os
from src.config import MONGO_URI, DB_NAME, COLLECTION_NAME


def get_customer_transactions(customer_id: int):

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]


    data = list(collection.find({"CustomerID": int(customer_id)}))

    if not data:
        return None

    df = pd.DataFrame(data)

    if "_id" in df.columns:
        df.drop("_id", axis=1, inplace=True)

    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

    return df




def compute_features(df):

    frequency = df["InvoiceNo"].nunique()
    monetary = df["TotalAmount"].sum()
    avg_order_value = monetary / frequency if frequency > 0 else 0

    return {
        "Frequency": frequency,
        "Monetary": monetary,
        "AvgOrderValue": avg_order_value
    }