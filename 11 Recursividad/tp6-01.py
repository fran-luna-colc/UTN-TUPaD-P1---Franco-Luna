"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
        

# Programa principal
print("Crear un factorial y el factorial de todos los numeros anteriores")
fac = int(input("Ingresar número: "))
for i in range (fac,0,-1):
    print(factorial(i))