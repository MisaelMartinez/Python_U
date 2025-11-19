from fastapi import FastAPI
from pydantic import BaseModel 


class User(BaseModel): 
    id: int
    nombre:str
    email:str
    edad: int | None =None 
    activo: bool

app = FastAPI()

@app.get("/users/")
def get_users():
    return 'Estas en el get'

@app.post("/users/") 
def create_user(user:User):
    return {"Mensaje": f'Usuario {user.nombre.capitalize()} creado exitosamente.',
            "datos": user}

#Modificamos la funcion original agregando q.
@app.put("/users/{user_id}")
def update_user(user_id:int,user: User, q: str | None =None):
    result: dict = {"user_id": user_id, **user.model_dump()}
    if q:
        result.update({"q":q})
    return result


#http://127.0.0.1:8000/users/27?q= esta url nos mostrara todo igual porque q esta vacia
#http://127.0.0.1:8000/users/27?q=hfksdhkj esta url nos mostrara que se agrego la q y su valor.
    