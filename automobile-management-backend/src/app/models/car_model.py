from odmantic import Model, Field
from datetime import datetime
from typing import Optional, Dict
from enum import Enum

class FuelType(str, Enum):
    PETROL = "petrol"
    DIESEL = "diesel"
    ELECTRIC = "electric"
    HYBRID = "hybrid"

class Transmission(str, Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"

class AdPlatform(str, Enum):
    HASZNALTAUTO = "hasznaltauto.hu"
    FACEBOOK = "facebook marketplace"


class Car(Model):
    brand: str
    model: str
    year: int
    license_plate: str = Field(unique=True)

    price: int
    mileage: int

    fuel_type: FuelType
    transimission: Transmission
    engine_power: int

    is_sold: bool = False
    purchase_date: datetime
    sale_date: Optional[datetime] = None

    ads: Dict[AdPlatform, str] = {}

    model_config = {
            "collection": "cars"
        }