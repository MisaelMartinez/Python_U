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


@app.put("/users/{user_id}")
def update_user(user_id:int,user: User):
    return {"user_id": user_id,**user.model_dump()}


#El **toma las claves de User y las agrega una por una al mismo nivel que user_id
#model_dump viene en los metodos de pydantic. Transformar un user a diccionario
#Antes de escribia como **user.dict() 

#En Postman abrimos un nuevo request. en PUT.
#Escribimos el url http://127.0.0.1:8000/users/2
#y en el Body - row escribimos 

# {
#     "id":"1",
#     "nombre":"Misael",
#     "email": "m@gmail.com",
#     activo:"false"
# }

#Revisamos que este en JSON al final del la fila de row.
#Guardamos y listo. SEND.


