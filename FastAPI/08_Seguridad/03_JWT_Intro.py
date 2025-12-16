#Esta JWT esta separada en tres partes.
# aaaa.bbbb.cccc Siempre estaran separadas por 3 puntos.

#Instalamos el paquete JWT con pip install PyJWT

import jwt
import datetime
#En https://www.browserling.com/tools/random-hex vamos a generar una cadena de 32 
SECRET_KEY = "01a58102c366a42e7c81ba7f4d1d6fd9"

payload: dict = {
    "username": "Eduardo Rios",
    "role": "admin",
    "exp": datetime.datetime.now(datetime.timezone.utc)+ datetime.timedelta(hours=1)

}

#Creas token.
token = jwt.encode(payload, SECRET_KEY, algorithm= "HS256")
print(f'\n{token}\n')

#El token que aparece en consola nos debe de proporcionar la informacion de nuestro dic en JWT.io.

#Verificar/decodificar token
try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print(f'\n {decoded} \n')
except jwt.ExpiredSignatureError:
    print("El token ha expirado.")
except jwt.InvalidTokenError:
    print('Token invalido.')

    










