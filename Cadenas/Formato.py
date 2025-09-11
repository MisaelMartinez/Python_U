"""
Python ofrece varias maneras de formatear cadenas , que incluye la capacidad de concatenar texto,
variables e incluso dar otro tipo de formato, como ndicar el numero de decimales en el formato.

- f.string(python 3.6+): Esta es la opcion para recomendada por ser la mas sencilla, rapida, y legible.
r = f'Hola {var}'

- metodo format: es versatil y poderoso.
r = 'Hola {}'.format(var)
"""

nombre = "Giss"
strr = "Hola"

#f.string
rf = f'Mi amiga me dijo {strr} y me llamo {nombre}'
print(rf)

#Format
rm = "Mi amiga me dijo {} y me llamo {}".format(strr,nombre)
print(rm)




