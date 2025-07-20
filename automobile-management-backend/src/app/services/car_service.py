from db import engine
from models.car_model import Car
from odmantic import ObjectId
from schemas.car_schema import CreateCar

async def get_all_cars():
    cars = await engine.find(Car)

    if cars:
        return cars
    
    return {"error": "List is empty"}

async def get_car_by_id(car_id: str):
    car = await engine.find_one(Car, Car.id == ObjectId(car_id))

    if car:
        return car
    
    return {"error": "Car not found"}

async def create_car(car_data: CreateCar):
    car = Car(**car_data.model_dump())
    await engine.save(car)

    return car