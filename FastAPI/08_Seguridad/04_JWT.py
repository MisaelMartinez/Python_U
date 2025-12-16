#Debemos de instalar con pip install "passlib[bcrypt]"
#Este sera el encargado de hashear nuestras contraseñas.

from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from fastapi import Depends,FastAPI,HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
#En un proyecto real esto no debe de estar aqui. deberia de ir a envieroment variables.

#Esto se encuentre en .env
# SECRET_KEY = "c9990297cd248de2afbe346d7ec0e5ba"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30
#Para mandarlas a llamar es necesario utilizar pip install dotenv

#Importamos el pack para el .env
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY") or "Valor_por_defecto"
ALGORITHM = os.getenv("ALGORITHM") or "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES") or 30)
#El or es una buena practica.

#HASHEO DE PASWORD
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password:str):
    return pwd_context.hash(password)

#FAKE_LIST

fake_user_DB :dict ={
    "jhondoe": {"username":"jhondoe",
                "email":"g@gmail.com",
                "full_name":"Juan Martinez",
                "hashed_password":get_password_hash("1"),#Utilizamos esta funcion para hashear. pero el 1 sigue siendo nuestra contraseña
                "disabled":False},
    "alice": {"username":"alice",
                "email":"a@gmail.com",
                "full_name":"Alice Martinez",
                "hashed_password":get_password_hash("2"),
                "disabled":True}
}

#Models

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str|None = None

class User(BaseModel):
    username: str
    email: str|None = None
    full_name: str|None = None
    disabled: bool|None = None

class UserDB(User):
    hashed_password: str

#AUTH HELPERS
def get_user(db: dict, username: str):
    if username in db:
        user_dict = db[username]
        return UserDB(**user_dict)
    
def authenticate_user(fake_db: dict, username: str, password:str):
    user = get_user(fake_db,username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data:dict, expires_delta: timedelta|None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc)+ expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

#FASTAPI
app = FastAPI()

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= "Credenciales no validas.",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    # if Token_data.username is None:
    #     raise credentials_exception
    user = get_user(fake_user_DB, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
async def get_current_active_user(current_user:Annotated[User, Depends(get_current_user)]):
                                if current_user.disabled:
                                    raise HTTPException(status_code=400, detail="Usuario inactivo")
                                return current_user 

#Routes
@app.post("/token", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
     user = authenticate_user(fake_user_DB, form_data.username, form_data.password)
     if not user:
          raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                              detail= "Incorrect username or password",
                              headers={"WWW-Authenticate": "Bearer"})
     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     access_token = create_access_token(data = {"sub": user.username},expires_delta=access_token_expires)
     return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
     return current_user


#Al final utilizamos pip install pydantic_settings, nose para que jaja


# en el post generamos el token.
#En el get pegamos el token del post y nos debe mostrar nuestra info.












