from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pydantic import BaseModel
app = FastAPI()

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="token") #Nombre que va a ir despues del /

class User(BaseModel):
    username : str
    email: str | None = None
    full_name : str|None = None
    disable: bool|None = None

class UserDB(User):
    hashed_password: str #contraseña codificada.
    
fake_user_DB :dict ={
    "jhondoe": {"username":"Gaspariin",
                "email":"g@gmail.com",
                "full_name":"Juan Martinez",
                "hashed_password":"fakehash1",
                "disable":False},
    "alice": {"username":"alice",
                "email":"a@gmail.com",
                "full_name":"Alice Martinez",
                "hashed_password":"fakehash2",
                "disable":True}
}

def fake_hash_password(password:str) ->str:
    return "fakehash" + password

def get_user(db: dict, username: str) -> UserDB|None:
    if username in db:
        return UserDB(**db[username])
    return None

def fake_decode_token(token: str) -> UserDB |None:
    return get_user(fake_user_DB, token)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

#Paso extra para ver si esta o no autorizado.
async def get_current_active_user(current_user: Annotated[UserDB, Depends(get_current_user)]):
    if current_user.disable:
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user 
#Termina el paso extra.

@app.post("/token")
async def login(form_data:Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_user_DB.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrecte username or password.")
    user = UserDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if hashed_password != user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password.")
    #Retornar token (username).
    return {"access_token": form_data.username, "token_type":"bearer"}



@app.get("/users/me")
async def read_users_me(current_user: Annotated[User,Depends(get_current_active_user)]):
    return current_user


#PASOS EN URL... http://127.0.0.1:8000/docs
#Darle en el candadito
#Ingresar el usuario y la contraseña sin el hash.

#Postman.
#Primero agregamos un POST. en la ruta http://127.0.0.1:8000/token
#Body - form_data. agregamos username y password y asignamos el valor de 
#jhondoe, 1, respectivamente y nos debe de mostrar nuestro token

#Con un get ingresamos a http://127.0.0.1:8000/users/me
#en authorization y escribimos "jhondoe" y nos aparecera nuestra informacion






