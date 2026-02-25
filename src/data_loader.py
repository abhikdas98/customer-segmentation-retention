from pymongo import MongoClient
import pandas as pd
from src.config import MONGO_URI, DB_NAME, COLLECTION_NAME

def load_data_from_mongo():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    data = list(collection.find())

    df = pd.DataFrame(data)

    # Remove MongoDB internal id column
    if "_id" in df.columns:
        df.drop("_id", axis=1, inplace=True)

    print("Data successfully loaded from MongoDB.")
    print(f"Shape: {df.shape}")
    
    return df