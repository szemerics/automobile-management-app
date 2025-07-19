from fastapi import FastAPI
from routes.car_routes import router as car_router
app = FastAPI()

app.include_router(car_router)