#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#   ● Niño/a: menor de 12 años.
#   ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#   ● Adulto/a: mayor o igual que 30 años.

edad=int(input("Ingresar la edad del usuario: "))
if edad < 12:
    print("El usuario es un niño")
elif edad < 18 and edad >= 12:
    print("El usuario es un adolescente")
elif edad < 30 and edad >= 18:
    print("El usuario es un adulto joven")
else:
    print("El usuario es un adulto")