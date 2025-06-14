"""
Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
"""

def deci_bin(decimal):
    if decimal==0:
        return "" # Este es el caso base, donde para el programa.
    else:
        #deci_bin(decimal // 2), se encarga de ir reduciendo el numero
        #str(decimal % 2), se encarga de ir almacenando el valor del bit
        return deci_bin(decimal // 2) + str(decimal % 2)
        
print("Programa para convertir decimal a binarios.")
n=int(input("Ingresar un número: "))
print(deci_bin(n))
