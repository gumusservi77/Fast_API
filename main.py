from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import User,Gender,Roles

app= FastAPI()

db: List[User] = [
    User(
        id= UUID("7303e575-7a8e-4315-9ac6-fb8f0cb2b6df"),
        first_name= 'haro',
        last_name= "sakoragi",
        gender=Gender.Male,
        roles=[Roles.student]
    ),
    User(
        id= UUID("d6014f97-fe89-47de-a508-bb2559455cb9"),
        first_name= 'rin',
        last_name= "kyuske",
        gender=Gender.Male,
        roles=[Roles.admin, Roles.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "mahta"}


@app.get("/api/v1/users")
async def fetch_users():
    return db; 
    
@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id":user.id}


@app.delete("/api/v1/users/{user_id}")
async def delet_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return  