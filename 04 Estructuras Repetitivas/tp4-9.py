"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""
suma = 0
for i in range (0,100):
    num=int(input("Ingresar un número: "))
    suma = suma + num

print(f"La media de los números ingresados es {suma/100}")