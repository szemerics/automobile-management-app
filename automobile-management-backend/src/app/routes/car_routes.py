from fastapi import APIRouter
from services import car_service
from schemas.car_schema import CreateCar

router = APIRouter()

@router.get('/get_cars')
async def get_cars():
   result = await car_service.get_all_cars()

   return result

@router.get('/{car_id}')
async def get_car_by_id(car_id: str):
   result = await car_service.get_car_by_id(car_id)

   return result

@router.post('/')
async def create_car(car_data: CreateCar):
   return await car_service.create_car(car_data)