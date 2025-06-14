"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
"""

def suma_digitos(n):
    if n<=9: #Si el valor es menor o igual que nueve, retorna el valor de n
        return n
    else:
        return suma_digitos(n//10)+suma_digitos(n%10) 

#suma_digitos(n//10), va dividiendo y quedandose con el valor de esa división
#suma_digitos(n%10), va dividiendo y quedandose con el resto
#ejemplo: n=101
#101//10 = 10 ; 101%10 = 1 ; 10+1=11 ;; 11//10=1 ; 11%10=1 , 1+1=2; n=2 entonces n<=9,
#por lo cual retorna n

#Programa Principal
print("Programa para calcular la suma de todos los digitos")
n=int(input("Ingresar un número: "))

print(suma_digitos(n))