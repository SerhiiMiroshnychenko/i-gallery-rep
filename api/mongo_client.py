import os
from pymongo import MongoClient
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv(dotenv_path='./.env.local')

MONGO_URL = os.environ.get("MONGO_URL", "mongo")
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "root")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)

mongo_client = MongoClient(
    host=MONGO_URL,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    port=int(MONGO_PORT)
)


def insert_test_document():
    """
    Insert a sample document to the test collection in the test db.
    """
    d_b = mongo_client.test
    test_collection = d_b.test_collection
    result = test_collection.insert_one({"name": "Serhii", "age": 41})
    print(result)
