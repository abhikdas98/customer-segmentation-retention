from pymongo import MongoClient
import pandas as pd
from src.config import MONGO_URI, DB_NAME, COLLECTION_NAME
from src.logger import logger


def seed_data():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    if collection.count_documents({}) > 0:
        print("MongoDB already contains data. Skipping seeding.")
        return

    print("Seeding MongoDB in safe batches...")

    chunk_size = 2000
    total_inserted = 0

    for chunk in pd.read_csv("/app/data/raw/online_retail.csv", chunksize=chunk_size):

        chunk.replace([float("inf"), float("-inf")], pd.NA, inplace=True)
        chunk.dropna(subset=["CustomerID"], inplace=True)

        chunk["CustomerID"] = pd.to_numeric(chunk["CustomerID"], errors="coerce")
        chunk.dropna(subset=["CustomerID"], inplace=True)
        chunk["CustomerID"] = chunk["CustomerID"].astype(int)

        records = chunk.to_dict(orient="records")

        if records:
            collection.insert_many(records, ordered=False)
            total_inserted += len(records)
            print(f"Inserted {total_inserted} records...")

    logger.info("MongoDB seeding complete.")
    print("Seeding finished successfully.")