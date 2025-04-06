"""
10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
"""

Hemisferio=str(input("Ingresar el hemisferio en el que se encuentre, \"S\" si es en el hemisferio sur y \"N\" si es en el norte): ").upper())
print ("Ingresar fecha en números.")
año=int(input("Ingresar año: "))
mes=int(input("Ingresar mes: "))
dia=int(input("Ingresar día: "))

# La lista para el hemisferio Norte
if Hemisferio == "N":

#La lista de los meses que son extrictamente de una estación
    if mes  in [1,2]:
        if mes == 1 or mes == 2:
         print ("Es invierno.")
    if mes  in [4,5]:
        if mes == 4 or mes == 5:
         print ("Es primavera.")
    if mes in [7,8]:
        if mes == 7 or mes == 8:
            print ("Es verano.")
    if mes in [10,11]:
        if mes == 10 or mes == 11:
            print ("Es Otoño.")

# La lista para los meses que tienen días en 2 estaciones
    elif mes in [12,3,6,9]:
        if mes == 12 and dia >= 21:
            print ("Es invierno.")
        elif mes == 12 and dia <= 20:
                print ("Es Otoño.")
        elif mes == 3 and dia <= 20:
            print ("Es invierno.")
        elif mes == 3 and dia >= 21:
                print ("Es primavera.")
        elif mes == 6 and dia <= 20:
            print ("Es primavera.")
        elif mes == 6 and dia >= 21:
                print ("Es verano.")
        elif mes == 9 and dia <= 20:
            print ("Es verano.")
        elif mes == 9 and dia >= 21:
                print ("Es Otoño.")

# La lista para el hemisferio Sur
elif Hemisferio == "S":

#La lista de los meses que son extrictamente de una estación
    if mes  in [1,2]:
        if mes == 1 or mes == 2:
         print ("Es verano.")
    if mes  in [4,5]:
        if mes == 4 or mes == 5:
         print ("Es itoño.")
    if mes in [7,8]:
        if mes == 7 or mes == 8:
            print ("Es invierno.")
    if mes in [10,11]:
        if mes == 10 or mes == 11:
            print ("Es primavera.")

# La lista para los meses que tienen días en 2 estaciones
    elif mes in [12,3,6,9]:
        if mes == 12 and dia >= 21:
            print ("Es verano.")
        elif mes == 12 and dia <= 20:
                print ("Es primavera.")
        elif mes == 3 and dia <= 20:
            print ("Es verano.")
        elif mes == 3 and dia >= 21:
                print ("Es otoño.")
        elif mes == 6 and dia <= 20:
            print ("Es otoño.")
        elif mes == 6 and dia >= 21:
                print ("Es invierno.")
        elif mes == 9 and dia <= 20:
            print ("Es invierno.")
        elif mes == 9 and dia >= 21:
                print ("Es primavera.")
else:
    print ("Error, ingresar hemisferio valido.")