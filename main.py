import azure.functions as func
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uvicorn

app = FastAPI(title="CarPool API", description="API for managing carpool services")

# In-memory database (replace with actual database in production)
carpools = []

class CarPool(BaseModel):
    id: Optional[int] = None
    driver_name: str
    car_model: str
    available_seats: int = Field(gt=0, description="Number of available seats must be greater than 0")
    departure_time: datetime
    departure_location: str
    destination: str
    price_per_seat: float = Field(gt=0, description="Price per seat must be greater than 0")
    is_active: bool = True

@app.get("/")
async def root():
    return {"message": "Welcome to CarPool API"}

@app.get("/carpools", response_model=List[CarPool])
async def get_carpools():
    return carpools

@app.get("/carpools/{carpool_id}", response_model=CarPool)
async def get_carpool(carpool_id: int):
    for carpool in carpools:
        if carpool.id == carpool_id:
            return carpool
    raise HTTPException(status_code=404, detail="CarPool not found")

@app.post("/carpools", response_model=CarPool)
async def create_carpool(carpool: CarPool):
    # Find the next available ID
    existing_ids = {c.id for c in carpools if c.id is not None}
    next_id = 1
    while next_id in existing_ids:
        next_id += 1
    carpool.id = next_id
    carpools.append(carpool)
    return carpool

@app.put("/carpools/{carpool_id}", response_model=CarPool)
async def update_carpool(carpool_id: int, updated_carpool: CarPool):
    for i, carpool in enumerate(carpools):
        if carpool.id == carpool_id:
            updated_carpool.id = carpool_id
            carpools[i] = updated_carpool
            return updated_carpool
    raise HTTPException(status_code=404, detail="CarPool not found")

@app.delete("/carpools/{carpool_id}")
async def delete_carpool(carpool_id: int):
    for i, carpool in enumerate(carpools):
        if carpool.id == carpool_id:
            carpools.pop(i)
            return {"message": "CarPool deleted successfully"}
    raise HTTPException(status_code=404, detail="CarPool not found")

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
