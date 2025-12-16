#OAuth 2 --> es lo mas modernos, delegar autenticaciones. Delega el inicio de sesion.
#Es muy util para accedder a recursos a nombre del usuario.

#OpenID connect. Mas conocida.
#OpenID, clasica, no tiene relacion con OAuth2, casi obsoleta.
#OpenaAPI, define la estructura de las APIs. Ayuda a que las API sean faciles de entender.

                #OAuth 2 flujo de password + Bearer token.
#Primer paso, Hacer algo ya protegido.
from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="token") #Nombre que va a ir despues del /

@app.get("/items/")
async def get_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
    

#En este caso cuando ingresamos a la ruta 
#http://127.0.0.1:8000/items/
#Nos indican que no estamos autenticados. con tan solo poner la linea 16-20.

#Para poder pasar la autenticacion es necesario ingresar a /docs. dar clic en Autorizar pero nos pedira datos a ingresar.













