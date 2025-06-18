import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")
API_URL = os.getenv("PUBLIC_API_URL")
SERVICE_KEY = os.getenv("SERVICE_KEY")
