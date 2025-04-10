"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
num=int(input("Ingresar un número: "))
inverso=0
inverso1=0
digito=(len(str(num))) # Esta variable guarda el largo en digitos del número

num=abs(num)
for i in range (digito,0,-1): # Va desde la cantidad de digitos hasta 0 restandole 1

    inverso1 = num % 10 # inverso1 toma el valor del resto del número por 10 
    num = num // 10 # Esto permite que num se vaya dividiendo perdiendo su ultimo digito y haciendo que este guarde ese valor

    inverso = inverso + inverso1 * (10**(i-1)) # Esto genera que el resto de inverso1 se multiplique por 10 elevado el numero del digito - 1 y que la variable guarde el valor
    # ejemplo 123 % 10 = 3 /// 0 + 3 * 10**2 = 300 /// 12 % 10 = 2 /// 300 + 2 + 10**1 = 320 /// 1 % 10 = 1 /// 321 + 1 * 10 **1 = 321


print(f"El orden de digitos inverso es {inverso}")
