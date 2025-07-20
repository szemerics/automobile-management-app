from fastapi import APIRouter
from services import car_service
from schemas.car_schema import CreateCar

router = APIRouter()

@router.get('/get_cars')
async def get_cars():
   return await car_service.get_all_cars()

@router.get('/{car_id}')
async def get_car_by_id(car_id: str):
   return await car_service.get_car_by_id(car_id)

@router.post('/')
async def create_car(car_data: CreateCar):
   return await car_service.create_car(car_data)

@router.delete('/')
async def delete_car(car_id: str):
   return await car_service.delete_car(car_id)

@router.put('/{car_id}')
async def update_car(car_id:str, car_data:CreateCar):
   return await car_service.update_car(car_id, car_data)