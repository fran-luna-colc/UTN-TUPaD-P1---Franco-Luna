"""
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
"""

def contar_digito(numero, digito):
    veces=0 #variable que se va a quedar con el numero
    if numero==0:
        return 0
    else:
        veces=numero%10 #variable que se queda con el ultimo numero
        if veces==digito:
            return contar_digito(numero//10,digito) + 1 #si el ultimo numero es igual al digito suma 1 el retorno y sigue con el resto de números
        else:
            return contar_digito(numero//10,digito) #si el ultimo numero no es igual al digito no suma y sigue con el resto de números
    
#Programa principal
print("Programa para contar cuantas veces aparacio un número")
n=int(input("Ingresar un número: "))
d=int(input("Ingresar el digito del 0 al 9 a encontrar: "))
while d>9 or d<0:
        d=int(input("Error, Ingresarun digito del 0 al 9 a encontrar: "))

print(contar_digito(n,d))
