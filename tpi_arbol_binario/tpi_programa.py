# Función para construir un árbol binario de búsqueda balanceado
def construir_arbol(lista):
    medio = len(lista) // 2  # Se elige el valor del medio como raíz para balancear
    raiz = lista[medio]
    # Se construyen los subárboles izquierdo y derecho recursivamente
    izquierda = construir_arbol(lista[:medio])
    derecha = construir_arbol(lista[medio+1:])
    return [raiz, izquierda, derecha]  # Se representa el nodo como una lista: [raíz, izquierda, derecha]

# Función para mostrar el árbol en consola de forma visual
def mostrar_arbol(arbol, nivel=0):
        mostrar_arbol(arbol[2], nivel + 1)  # Muestra el subárbol derecho primero (arriba)
        print("   " * nivel + str(arbol[0]))  # Muestra el nodo con sangría según el nivel
        mostrar_arbol(arbol[1], nivel + 1)  # Muestra el subárbol izquierdo

# Función para buscar un valor en el árbol y contar los pasos
def buscar_en_arbol(arbol, valor, pasos=0):
    pasos += 1
    if valor == arbol[0]:  # Si el valor está en la raíz del nodo actual
        return True, pasos
    elif valor < arbol[0]:  # Si el valor es menor, buscamos a la izquierda
        return buscar_en_arbol(arbol[1], valor, pasos)
    else:  # Si es mayor, buscamos a la derecha
        return buscar_en_arbol(arbol[2], valor, pasos)

# Sección principal del programa

# Paso 1: Solicitar entre 5 y 9 números al usuario
numeros = []
print("Ingresá entre 5 y 9 números (uno por uno):")

while len(numeros) < 9:
    try:
        numero = int(input(f"Ingresá el número #{len(numeros)+1}: "))
        numeros.append(numero)
        if 5 <= len(numeros) < 9:
            continuar = input("¿Querés ingresar otro número? (s/n): ").lower()
            if continuar != 's':  # Si el usuario no quiere seguir, se corta el ingreso
                break
    except:  # Si se ingresa algo que no es un número
        print("Por favor, ingresá un número válido.")

# Ordenamos la lista antes de construir el árbol
numeros.sort()
arbol = construir_arbol(numeros)

# Mostrar el árbol construido
print("\nÁrbol binario balanceado creado:")
mostrar_arbol(arbol)

# Paso 2: Permitir al usuario buscar un número en el árbol
while True:
    try:
        valor_buscar = int(input("\n¿Querés buscar un número en el árbol? Ingresá un número: "))
        encontrado, pasos = buscar_en_arbol(arbol, valor_buscar)
        if encontrado:
            print(f"El número {valor_buscar} fue encontrado en {pasos} paso(s).")
            break  # Si se encuentra, se termina la búsqueda
        else:
            print(f"El número {valor_buscar} no se encontró en el árbol.")
            repetir = input("¿Querés buscar otro número? (s/n): ").lower()
            if repetir != 's':  # Si el usuario no quiere buscar más, se termina
                break
    except:  # Si se ingresa algo no válido
        print("Por favor, ingresá un número válido.")
