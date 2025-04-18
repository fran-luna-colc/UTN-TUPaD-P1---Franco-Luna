"""
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""

from math import pi #importar la constante de pi del modulo de math

#función calcular_area_circulo
def calcular_area_circulo(radio):
    return float((pi*(radio ** 2)))

#función calcular_perimetro_circulo
def calcular_perimetro_circulo(radio):
    return (2*pi*radio)

#función principal
radio = int(input("Ingresar el radio de un circulo: "))

print(f"Dado el radio de {radio}, su area es {calcular_area_circulo(radio)} y su perimetro es {calcular_perimetro_circulo(radio)}")
