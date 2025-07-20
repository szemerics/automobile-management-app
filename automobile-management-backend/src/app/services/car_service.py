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

async def delete_car(car_id: str):
    car = await engine.find_one(Car, Car.id == ObjectId(car_id))

    if not car:
        return {"error": "Car not found"}
    
    await engine.delete(car)
    return {"message": "Car deleted successfully"}

async def update_car(car_id: str, car_data: CreateCar):
    car = await engine.find_one(Car, Car.id == ObjectId(car_id))

    if not car:
        return {"error": "Car not found"}
    
    car.brand = car_data.brand
    car.model = car_data.model
    car.year = car_data.year
    car.license_plate = car_data.license_plate
    car.price = car_data.price
    car.mileage = car_data.mileage
    car.fuel_type = car_data.fuel_type
    car.transimission = car_data.transimission
    car.engine_power = car_data.engine_power
    car.is_sold = car_data.is_sold
    car.purchase_date = car_data.purchase_date
    car.sale_date = car_data.sale_date
    car.ads = car_data.ads

    await engine.save(car)
    
    return {"message": "Car updated successfully"}