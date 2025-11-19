from fastapi import FastAPI
from pydantic import BaseModel #Define los modelos.

#BaseModel, Saber que vamos a recibir. Validacion automatica a nuestro objeto.
class User(BaseModel): #Nos valida y/o convierte a int, str, o bool las variables de nuestra clase
    id: int
    nombre:str
    email:str
    edad: int | None =None# | None = None significa que es NO OBLIGATORIO
    activo: bool

app = FastAPI()

@app.get("/users/")
def get_users():
    return 'Estas en el get'

@app.post("/users/") #Mandar informacion del servidor
def create_user(user:User):
    return {"Mensaje": f'Usuario {user.nombre.capitalize()} creado exitosamente.',
            "datos": user}


"""
{
    "id": "1",
    "nombre":"Misael",
    "email": "m@gmail.com",
    "edad": "20" ,
    "activo": true
}
Ingresamos estos datos en el body en postman y en lugar de GET, usamos POST.
Recordemos que la edad debido al | None = None podemos no ponerla
"""




