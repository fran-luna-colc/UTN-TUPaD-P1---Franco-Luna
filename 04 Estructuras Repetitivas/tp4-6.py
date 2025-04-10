"""
6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
"""

num=int(input("Ingresar un número: "))

for i in range (1,11,1):
    print (f"{num} * {i} = {num*i}")
