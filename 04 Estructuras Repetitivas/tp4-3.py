"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.

"""

num1=int(input("Ingresar primer número: "))
num2=int(input("Ingresar segundo número: "))
acumulador=0

if num2>num1:
    for i in range (num1+1,num2,1):
        print (i)
        acumulador = acumulador + i
else:
    for i in range (num2+1,num1,1):
        print (i)
        acumulador = acumulador + i

print(f"La suma de todos los números entre el primer y el segundo número ingresado es {acumulador}")