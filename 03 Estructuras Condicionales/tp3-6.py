#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

num_aleatorios = {random.randint(1,100) for i in range (50)}

print (mode (num_aleatorios))
print (median (num_aleatorios))
print (mean (num_aleatorios))

if mean (num_aleatorios) > median (num_aleatorios) and median(num_aleatorios) > mode(num_aleatorios):
    print("Sesgo positivo.")
elif mean (num_aleatorios) < median (num_aleatorios) and median(num_aleatorios) < mode(num_aleatorios):
    print("Sesgo negativo.")
elif mean (num_aleatorios) == median (num_aleatorios) and median(num_aleatorios) == mode(num_aleatorios):
    print ("Sin sesgo.")
else:
    pass