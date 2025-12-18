from fastapi import APIRouter
from pydantic import BaseModel
from main import app
from database import SessionLocal, engine
from models import Booking

booking_router = APIRouter()

class BookingIn(BaseModel):
    user_id: int
    hotel_id: int
    check_in: str
    check_out: str
    price: float

class BookingOut(BaseModel):
    booking_id: int
    user_id: int
    hotel_id: int
    check_in: str
    check_out: str
    price: float

@app.get("/bookings", response_model=List[BookingOut])
def get_bookings():
    db = SessionLocal()
    bookings = db.query(Booking).all()
    return bookings
