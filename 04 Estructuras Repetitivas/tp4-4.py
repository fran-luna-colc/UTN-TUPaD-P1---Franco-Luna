"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
suma=0

print("Suma de números, ingresar 0 cuando quiera parar la suma")
num=int(input("Ingresar un número: "))

while num != 0:
    suma = suma + num    
    num=int(input("Ingresar un número: "))

print(f"La suma de los números da como resultado {suma}")