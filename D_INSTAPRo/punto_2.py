def ordenar_nombres(nombres):
    # Ordenar la lista de nombres
    nombres_ordenados = sorted(nombres)

    # Imprimir los nombres en orden alfabético
    print("Lista de nombres en orden alfabético:")
    for nombre in nombres_ordenados:
        print(nombre)


# Leer la cantidad de nombres
cantidad = int(input("¿Cuántos nombres deseas ingresar? "))
nombres = []

# Leer los nombres del usuario
for _ in range(cantidad):
    nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)

# Llamar a la función para ordenar e imprimir los nombres
ordenar_nombres(nombres)
