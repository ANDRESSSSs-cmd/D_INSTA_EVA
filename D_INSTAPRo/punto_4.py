def sumar_numeros_pares(numeros):
    suma = 0  # Inicializar la suma en 0

    # Recorrer cada número en la lista
    for numero in numeros:
        if numero % 2 == 0:  # Verifica si el número es par
            suma += numero  # Sumar el número par a la suma

    return suma


# Leer la cantidad de números
cantidad = int(input("¿Cuántos números deseas ingresar? "))
numeros = []

# Leer los números del usuario
for _ in range(cantidad):
    numero = int(input("Ingresa un número: "))
    numeros.append(numero)

# Calcular e imprimir la suma de los números pares
suma_pares = sumar_numeros_pares(numeros)
print("La suma de los números pares es:", suma_pares)
