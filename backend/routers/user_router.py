from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from main import app
from database import SessionLocal, engine
from models import User
from typing import List

user_router = APIRouter()

class UserIn(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    user_id: int
    username: str
    email: str

@app.post("/auth/register", response_model=UserOut)
def register(user: UserIn):
    db = SessionLocal()
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid user")
    if form_data.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")
    return {"access_token": user.username, "token_type": "bearer"}
