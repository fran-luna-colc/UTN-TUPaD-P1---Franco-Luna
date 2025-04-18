"""
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""
# función celsius_a_fahrenheit
def celsius_a_fahrenheit(celsius):
    temperatura = (celsius * (9/5)) + 32 
    return temperatura

# función principal
cel = int(input("Ingresar una temperatura en Celcius: "))

temp = celsius_a_fahrenheit(cel)
print (f"La temperatura de {cel}° celsius a fahrenheit es {temp}°")