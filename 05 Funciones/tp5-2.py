"""
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""
# Función nueva saludar_usuario
def saludar_usuario(nombre):
    return (f"Buenos días {nombre}!")

# Función principal / Programa principal
nombre=input("Ingresar nombre: ")

print(saludar_usuario(nombre))