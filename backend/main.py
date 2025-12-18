from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user_router, hotel_router, booking_router

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(hotel_router)
app.include_router(booking_router)
