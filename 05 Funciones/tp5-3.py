"""
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""
# Función nueva
def informacion_personal(nombre, apellido, edad, residencia):
    return (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Función principal / Programa principal
nombre =input("Ingresar nombre: ")
apellido =input("Ingresar apellido: ")
edad =input("Ingresas edad: ")
residencia =input("Ingresar residencia: ")

print (informacion_personal(nombre,apellido,edad,residencia))