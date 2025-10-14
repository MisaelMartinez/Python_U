"""
Crear un programa para generar un email a partir de los siguientes datos

Nombre     Juan Misael Martinez
Empresa     Samsung
dominio     .com.mx

email final
juan_misael_martinez@samsung.com.mx
"""


name = "Juan Misael Martinez"
empresa = "Samsung"
dominio = ".com.mx"

name_l = name.replace(" ", "_")

e_mail = "".join([name_l.lower(),"@",empresa.lower(),dominio])

print(f"Nombre del usuario: {name}")
print(f'Nombre de la empresa: {empresa}')
print(f'\nTu correo asignado sera: ')

print(e_mail)




