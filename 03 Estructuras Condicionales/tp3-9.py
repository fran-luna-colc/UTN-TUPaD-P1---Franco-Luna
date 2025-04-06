"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
"""

terremoto=float(input("Ingresar la magnitud del terremoto: "))

if terremoto < 3:
    print ("Muy leve (imperceptible).")
elif terremoto >= 3 and terremoto < 4:
    print ("Leve (ligeramente perceptible).")
elif terremoto >= 4 and terremoto < 5:
    print ("Moderado (sentido por personas, pero generalmente no causa daños).")
elif terremoto >= 5 and terremoto < 6:
    print ("Fuerte (puede causar daños en estructuras débiles).")
elif terremoto >= 3 and terremoto < 7:
    print ("Muy fuerte (puede causar daños significativos).")
elif terremoto >= 7:
    print ("Extremo (puede causar graves daños a gran escala).")