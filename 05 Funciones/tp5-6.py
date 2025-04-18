"""
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""
# Función tabla_multiplicar
def tabla_multiplicar(numero):
    for i in range(1,11):
        tabla = numero*i
        print (tabla)
    return tabla

# Función principal
num = int(input("Ingresar un número: "))

tabla_multiplicar(num)