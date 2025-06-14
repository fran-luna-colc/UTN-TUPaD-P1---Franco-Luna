"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique
"""

def fibona(num):
    if num==0 or num==1:
        return num
    else:
        return fibona(num-1) + fibona(num-2)


# Programa Principal
print("Crear serie Fibonacci")
n = int(input("Ingresar un número: "))
for i in range (0,n):
    print(fibona(i))
