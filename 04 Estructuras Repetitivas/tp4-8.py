"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

positivo = 0
negativo = 0
par = 0
impar = 0

for i in range (0,100):
    num=int(input("Ingresar un número: "))
    if num > 0:
        positivo += 1
    else:
        negativo += 1
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print (f"La cantidad de números positivos es {positivo}, la de negativos es {negativo}, la de pares es {par} y la de impares {impar}")
