"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""

num=int(input("Ingresar un número entero: "))
contador=0

while num >= 1:

    contador += 1

    num = num // 10

print("La cantidad de digitos son",contador)