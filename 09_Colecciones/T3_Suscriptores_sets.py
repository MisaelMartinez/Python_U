print('Lista de suscriptores')

suscriptores = {'luisa@mail.com','marcos@mail.com','elena@mail.com'}
#Verificar si un nuevo suscriptor ya esta en la lista

new_suscriptor = 'marcos@mail.com'
if new_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya esta en la lista')
else:
    suscriptores.add(new_suscriptor)
    print('El nuevo suscriptor ha sido agregado')

#Eliminar suscriptor
s_delete = 'elena@mail.com'
suscriptores.remove(s_delete)
print('Elena ha sido eliminada')

#Cantidad total de suscriptores
print(f'La cantidad de elementos total es: {len(suscriptores)}')










