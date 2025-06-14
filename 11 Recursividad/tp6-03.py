"""
3) Crea una función recursiva que calcule 
la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1).
 Prueba esta función en un algoritmo general.
"""

def pot_recur(n,m):
    if m==0:
        return 1
    else:
        return n*pot_recur(n,m-1)

#Programa Principal
print("Programa para calcular la potencia")
n=int(input("Ingresar la base de número: "))
m=int(input("Ingresar el exponente de número: "))
print(pot_recur(n,m))