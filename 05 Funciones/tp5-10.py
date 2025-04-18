"""
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""
# función calcular_promedio(a, b, c)
def calcular_promedio(a, b, c):
    promedio = (a+b+c)/3
    return promedio

# función principal
num1 = float(input("Ingresar el primer valor: "))
num2 = float(input("Ingresar el segundo valor: "))
num3 = float(input("Ingresar el tercer valor: "))

promedio = calcular_promedio(num1,num2,num3)

print (f"El promedio de los 3 valores previos es {promedio}")