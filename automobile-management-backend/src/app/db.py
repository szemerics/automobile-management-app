from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from config import settings

client = AsyncIOMotorClient(settings.MONGODB_URI)
engine = AIOEngine(client=client, database=settings.DATABASE_NAME)