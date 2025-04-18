"""
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
 restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""
# Función operaciones_basicas
def operaciones_basicas(a, b):
    ope = (a+b, a-b, a*b, a/b)
    return ope

# Función principal
num1=int(input("Ingresar el primer número: "))
num2=int(input("Ingresar el segundo número: "))

ope = operaciones_basicas(num1,num2)

# Invocación de los valores alojados en el tuple "ope"
print (f"Los valores {num1} y {num2} sumados son {ope[0]}, restados {ope[1]}, multiplicados {ope[2]} y divididos {ope[3]}")