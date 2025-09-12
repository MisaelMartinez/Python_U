"""
Python ofrece varias maneras de formatear cadenas , que incluye la capacidad de concatenar texto,
variables e incluso dar otro tipo de formato, como ndicar el numero de decimales en el formato.

- f.string(python 3.6+): Esta es la opcion para recomendada por ser la mas sencilla, rapida, y legible.
r = f'Hola {var}'

- metodo format: es versatil y poderoso.
r = 'Hola {}'.format(var)
"""

nombre = "Diana"
strr = "Hola"

#f.string
rf = f'Mi novia me dijo {strr} y se llama {nombre}'
print(rf)

#Format
rm = "Mi novia me dijo {} y se llama {}".format(strr,nombre)
print(rm)




