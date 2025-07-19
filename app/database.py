import motor.motor_asyncio
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv not installed, using system environment variables")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "defaultdb")

if not MONGO_URI or not DB_NAME:
    raise ValueError("MONGO_URI and DB_NAME environment variables must be set")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
