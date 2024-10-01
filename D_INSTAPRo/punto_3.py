def filtrar_palabras_por_letra(palabras, letra):
    # Lista para almacenar las palabras que comienzan con la letra dada
    palabras_filtradas = []

    # Recorre cada palabra en la lista
    for palabra in palabras:
        if palabra.startswith(letra):  # Verifica si la palabra comienza con la letra
            palabras_filtradas.append(palabra)  # Agrega la palabra a la lista filtrada

    return palabras_filtradas


# Leer la cantidad de palabras
cantidad = int(input("¿Cuántas palabras deseas ingresar? "))
palabras = []

# Leer las palabras del usuario
for _ in range(cantidad):
    palabra = input("Ingresa una palabra: ")
    palabras.append(palabra)

# Leer la letra con la que deben comenzar las palabras
letra = input("Ingresa la letra con la que deben comenzar las palabras: ")

# Filtrar e imprimir las palabras
resultados = filtrar_palabras_por_letra(palabras, letra)
print("Palabras que comienzan con la letra '{}':".format(letra))
for palabra in resultados:
    print(palabra)
