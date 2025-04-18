"""
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""
# función segundos_a_horas
def segundos_a_horas(segundos):
    return ((segundos/60)/60)

# función principal
segundos = int(input("Ingresar la cantidad de segundos que quiere convertir a horas: "))

print(f"La cantidad de {segundos} segundos equivale a {segundos_a_horas(segundos)} horas.")