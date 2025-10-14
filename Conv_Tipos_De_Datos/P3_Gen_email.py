"""
Crear un programa para generar un email a partir de los siguientes datos

Nombre     Juan Misael Martinez
Empresa     Samsung
dominio     .com.mx

email final
juan_misael_martinez@samsung.com.mx
"""

print('*** Generado de email***')
name = input('Ingresa tu nombre completo: ')
empresa = input('¿En que empresa trabajas?' )
ext = '.com.mx'

email = name.strip().replace(" ",'_').lower() + '@' + empresa.strip().lower() + ext


print(f'\n Hola {name}. \n Tu email es: {email}')