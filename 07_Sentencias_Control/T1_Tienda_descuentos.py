"""
Crear un sistema que ofrezca descuenos dependiendo del monto de la compra o si es miembro de la tienda.

*Si ha comprado mas de 100 pesos, 10% de descuento
*Solo miembro, 5% de descuento
*Si no es miembro y compro menos de 100, no hay descuencto.

"""



x = 101.5555
y = input('Eres miembro de nuestra tienda? ')

if y.lower().strip() == 'si':
    y = True
else:
    y= False

print(f'El monto de la compra es: {x:.2f}')

if x>= 100: #Compro mas de 100 pesos
    print(f'El total a pagar es: {x*0.9:.2f} pesos porque compraste mas de 100 ') #Imprimir mensaje
elif y== True: #Es miembro?
    print(f'El total a pagar es: {x*0.95:.2f} peses porque eres miembro')#Imprime mensaje
else:
    print(f'El total a pagar es: {x}')





