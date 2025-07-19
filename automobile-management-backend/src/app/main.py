from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine, ObjectId

from config import settings

from models.movie import Movie


app = FastAPI()

client = AsyncIOMotorClient(settings.MONGODB_URI)
engine = AIOEngine(client=client, database=settings.DATABASE_NAME)

print(settings.DATABASE_NAME)


@app.get('/movie/{movie_id}')
async def get_movie_by_id(movie_id: str):
    movie = await engine.find_one(Movie, Movie.id == ObjectId(movie_id))

    if movie:
        return movie
    
    return {"error": "Movie not found"}