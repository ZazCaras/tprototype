import os

from pymongo import MongoClient

MONGO_HOSTNAME = os.environ["MONGO_HOSTNAME"]
MONGO_PORT = os.environ["MONGO_PORT"]
MONGO_INITDB_DATABASE = os.environ["MONGO_INITDB_DATABASE"]
MONGO_INITDB_ROOT_USERNAME = os.environ["MONGO_INITDB_ROOT_USERNAME"]
MONGO_INITDB_ROOT_PASSWORD = os.environ["MONGO_INITDB_ROOT_PASSWORD"]

client = MongoClient(
    f"mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@{MONGO_HOSTNAME}:{MONGO_PORT}/"
)
db = client[MONGO_INITDB_DATABASE]

try:
    client.admin.command('ismaster')
    print("MongoDB connection successful")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")