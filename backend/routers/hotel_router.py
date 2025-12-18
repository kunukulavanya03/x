from fastapi import APIRouter
from pydantic import BaseModel
from main import app
from database import SessionLocal, engine
from models import Hotel

hotel_router = APIRouter()

class HotelIn(BaseModel):
    name: str
    city: str
    description: str
    rating: int

class HotelOut(BaseModel):
    hotel_id: int
    name: str
    city: str
    description: str
    rating: int

@app.get("/hotels", response_model=List[HotelOut])
def get_hotels():
    db = SessionLocal()
    hotels = db.query(Hotel).all()
    return hotels
