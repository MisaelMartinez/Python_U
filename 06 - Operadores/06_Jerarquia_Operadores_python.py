"""
La jerarquia de operadores determina el orden en que se calculan las operaciones en una expresion
Python aplica la siguiente tabla para egurar que algunos operadores tengan mayor prioridad que otros.

1. ()
2. **
3. +x, -x
4. *,/,//,%
5. +, -
6. ==, !=, <, <=, >, >=
7. and, or, not
8. =, +=, -=, ...
"""
#Ejemplos

r = 5+3*2**2
print(r)
r= (5*3)**2*2
print(r)

