from pymongo import MongoClient
import pandas as pd
import os
from src.config import MONGO_URI, DB_NAME, COLLECTION_NAME
from src.logger import logger


def seed_data():
    try:
        logger.info("Connecting to MongoDB...")
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        # Check if already populated
        if collection.count_documents({}) > 0:
            logger.info("MongoDB already contains data. Skipping seeding.")
            return

        logger.info("Seeding MongoDB...")

        file_path = os.path.join("data", "raw", "online_retail.csv")

        if not os.path.exists(file_path):
            logger.error(f"CSV file not found at path: {file_path}")
            return

        df = pd.read_csv(file_path)

        # Clean data
        df.replace([float("inf"), float("-inf")], pd.NA, inplace=True)
        df.dropna(subset=["CustomerID"], inplace=True)

        df["CustomerID"] = pd.to_numeric(df["CustomerID"], errors="coerce")
        df.dropna(subset=["CustomerID"], inplace=True)
        df["CustomerID"] = df["CustomerID"].astype(int)

        records = df.to_dict(orient="records")

        if records:
            collection.insert_many(records)
            logger.info(f"Successfully inserted {len(records)} records into MongoDB.")
        else:
            logger.warning("No records found to insert.")

    except Exception as e:
        logger.error(f"Error during MongoDB seeding: {e}")


if __name__ == "__main__":
    seed_data()