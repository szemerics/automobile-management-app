from db import engine
from models.car import Car
from odmantic import ObjectId

async def get_car_by_id(car_id: str):
    car = await engine.find_one(Car, Car.id == ObjectId(car_id))

    if car:
        return car
    
    return {"error": "Car not found"}