# Autor: Alba Segura

#Importem les llibreries FastAPI, HTTPException, BaseModel, List, users i db_users
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import users
import db_users
import rooms
import db_rooms
import access
import db_access
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
#Inicialitzem la nostra aplicació FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
###########
# CLASSES #
###########
class User(BaseModel):    
    id: int
    name: str                      
    surname: str
    username: str     
    DNI: str       
    password: str   
    email: str    
    groups: str    
    rol: str   
    created_at: str
    updated_at: str

class Rooms(BaseModel):
    id: int
    name: str
    description: str
    building_name: str
    created_at: str
    updated_at: str

class Access(BaseModel):
    id: int
    user_id: int
    room_id: int
    entry_time: str
    exit_time: str
    entry_date: str
    exit_date: str
    created_at: str
    updated_at: str

class UserC(BaseModel):
    name: str                      
    surname: str
    username: str     
    DNI: str       
    password: str   
    email: str    
    groups: str  

class RoomsC(BaseModel):
    name: str
    description: str
    building_name: str

class AccessC(BaseModel):
    user_id: int
    room_id: int
    entry_time: str
    exit_time: str
    entry_date: str
    exit_date: str

class UserU(BaseModel):
    name: str                      
    surname: str
    username: str     
    DNI: str       
    password: str   
    email: str    
    groups: str  
    rol: str
#############
# Endpoints #
#############

#Endpoint per a la pàgina principal
@app.get("/")
def read_root():
    return {"message": "API PROJECTE A05-5"}

#Endpoint per a la llista d'users
@app.get("/users", response_model=List[User])
def read_users():
    return users.users_schema(db_users.read())

#Endpoint per a mostrar un user per id
@app.get("/user/show/{id}", response_model=User)
def read_users_id(id: int):
    user = db_users.read_id(id)
    if user is not None:
        return users.user_schema(user)
    else:
        raise HTTPException(status_code=404, detail="Item not found")
        
@app.get("/users/getUsername/{username}")
async def get_user_by_username(username: str):
    user = db_users.get_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "username": user[3],  # Assuming username is at index 2
        "password": user[5],  # Assuming password is at index 5
        "rol": user[8]       # Assuming role is at index 8
    }
    
#Endpoint per a la llista d'users
@app.get("/rooms", response_model=List[Rooms])
def read_rooms():
    return rooms.rooms_schema(db_rooms.read())

#Endpoint per a mostrar un user per id
@app.get("/room/show/{id}", response_model=Rooms)
def read_rooms_id(id: int):
    room = db_rooms.read_id(id)
    if room is not None:
        return rooms.room_schema(room)
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.get("/access", response_model=List[Access])
def read_access():
    acces = db_access.read()
    if acces is not None:
        return access.access_schema(acces)
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/access/show/{id}", response_model=Access)
def read_access_id(id: int):
    acces = db_access.read_id(id)
    if acces is not None:
        return access.acces_schema_id(acces[0])
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/access/show_user/{id}", response_model=List[Access])
def read_access_user(id: int):
    acces = db_access.read_by_user_id(id)
    if acces is not None:
        return access.access_schema_id(acces)
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/access/show_room/{id}", response_model=List[Access])
def read_access_room(id: int):
    acces = db_access.read_by_room_id(id)
    if acces is not None:
        return access.access_schema_id(acces)
    else:
        raise HTTPException(status_code=404, detail="Item not found")



@app.post("/user/addAlumn")
def add_alumn(user: UserC):
    try:
        result = db_users.add_alumn(user.name, user.surname, user.username, user.DNI, user.password, user.email, user.groups)
        if result["status"] == -1:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error adding user: {e}")

@app.post("/user/addProf")
def add_prof(user: UserC):
    try:
        result = db_users.add_prof(user.name, user.surname, user.username, user.DNI, user.password, user.email, user.groups)
        if result["status"] == -1:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error adding user: {e}")

@app.post("/user/addAdmin")
def add_admin(user: UserC):
    try:
        result = db_users.add_admin(user.name, user.surname, user.username, user.DNI, user.password, user.email, user.groups)
        if result["status"] == -1:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error adding user: {e}")

@app.post("/room/addRoom")
def add_room(room: RoomsC):
    try:
        result = db_rooms.add_room(room.name, room.description, room.building_name)
        if result["status"] == -1:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error adding room: {e}")

@app.post("/access/addAccess")
def add_access(access: AccessC):
    try:
        result = db_access.add_access(access.user_id, access.room_id, access.entry_time, access.entry_date, access.exit_time, access.exit_date)
        if result["status"] == -1:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error adding access: {e}")

@app.put("/user/update/{id}")
def update_user(id: int, user: UserU):
    try:
        id_exists = db_users.read_id(id)
        if id_exists is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = db_users.updt_user(id, user.name, user.surname, user.username, user.DNI, user.password, user.email, user.groups, user.rol)
        if result["status"] == -1:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating user: {e}")

@app.put("/room/update/{id}")
def update_room(id: int, room: RoomsC):
    try:
        id_exists = db_rooms.read_id(id)
        if id_exists is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = db_rooms.updt_room(id, room.name, room.description, room.building_name)
        if result["status"] == -1:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating room: {e}")

@app.put("/access/update/{id}")
def update_access(id: int, access: AccessC):
    try:
        id_exists = db_access.read_id(id)
        if id_exists is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = db_access.updt_access(id, access.user_id, access.room_id, access.entry_time, access.entry_date, access.exit_time, access.exit_date)
        if result["status"] == -1:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating access: {e}")

@app.delete("/user/delete/{id}")
def del_user(id: int):
    try:
        id_exists = db_users.read_id(id)
        if id_exists is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = db_users.del_user(id)
        if result["status"] == -1:
            raise HTTPException(status_code=400, detail=result["message"])
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error removing user: {e}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)