# Instalamos FastAPI con el comando en la terminal  -- pip install "fastapi[standard]"
# Nuestra primer FastAPI
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hola mundo!!!"}

#Ejecutamos el codigo con 
#fastapi dev Hola_Mundo.py
#Es necesario llamar app, importar fastAPI y estar en la carpeta del archivo

#Podemos instalar una extension de JSON en chrome
#JSON Viewer Pro

#http://127.0.0.1:8000/docs  
#http://127.0.0.1:8000/redoc  
#http://127.0.0.1:8000/openapi.json --Descripcion de nuestra API.


#Con CTRL+C se detiene el servidor