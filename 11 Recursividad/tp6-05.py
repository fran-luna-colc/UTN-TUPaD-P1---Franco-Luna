"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
"""

def es_palindromo(palabra):
    if len(palabra)<=1: # Si la palabra tiene 1 o 0 caracteres es verdadera
        return True
    elif palabra[0] != palabra[-1]: # Si la palabra empieza y termina con caracteres distintos
        return False
    else:
        return es_palindromo(palabra[1:-1]) # En cada ciclo se van perdiendo el primer y el ultimo caracter

#Neuquen  
#euque
#uqu
#q = True
    
#Programa principal
print("Programa para saber si una palabra es palíndromo.")
palabra=str(input("Ingresar una palabra: "))
print(es_palindromo(palabra))