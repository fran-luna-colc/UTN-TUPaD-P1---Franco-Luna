"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

num=int(input("Ingresar un número: "))
suma=0

for i in range (0,num):
    suma = suma + i

print (F"La suma de todos los números entre 0 y el número ingresado es {suma}")