from database import Base
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

class Hotel(Base):
    __tablename__ = "hotels"
    hotel_id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    description = Column(String)
    rating = Column(Integer)

class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    hotel_id = Column(Integer)
    check_in = Column(Date)
    check_out = Column(Date)
    price = Column(Float)
