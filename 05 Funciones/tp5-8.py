"""
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""
# Función calcular_imc
def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    return imc

# Función principal
peso = (float(input("Ingresar el peso en kilogramos: ")))
altura = (float(input("Ingresar la altura en metros: ")))

if altura > 3: #por si alguien pone la altura en centimetros, esto hace que pase a metros
    altura = altura / 100

imc = int(calcular_imc(peso,altura))

print (f"Dado un peso de {peso} kg y una altura de {altura} metros, el indice de masa corporal es de {imc}")