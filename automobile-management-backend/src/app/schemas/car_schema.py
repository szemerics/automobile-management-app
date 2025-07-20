from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict

from models.car_model import FuelType, Transmission, AdPlatform

class CreateCar(BaseModel):
    brand: str
    model: str
    year: int
    license_plate: str

    price: int
    mileage: int

    fuel_type: FuelType
    transimission: Transmission
    engine_power: int

    is_sold: bool = False
    purchase_date: datetime
    sale_date: Optional[datetime] = None

    ads: Dict[AdPlatform, str] = {}