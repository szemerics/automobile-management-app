from fastapi import APIRouter
from services import car_service

router = APIRouter()

@router.get('/cars/{car_id}')
async def get_car_by_id(car_id: str):
   result = await car_service.get_car_by_id(car_id)

   return result