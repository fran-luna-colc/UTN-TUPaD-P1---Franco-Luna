"""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random

num=int(input("Ingresar un número entre 0 y 9: "))
rand=random.randint(0,9)
contador=1

while num != rand:
    num=int(input("Ingresar un número entre 0 y 9: "))
    contador += 1

print(f"El número es {rand} y la cantidad de intentos fueron {contador}")