def contar_vocales(frase):
    # Inicializar contadores para cada vocal
    conteo_vocales = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    # Convertir la frase a minúsculas para contar sin distinción
    frase = frase.lower()

    # Recorrer cada carácter en la frase
    for letra in frase:
        if letra in conteo_vocales:  # Verificar si la letra es una vocal
            conteo_vocales[letra] += 1  # Incrementar el contador correspondiente

    # Mostrar el conteo de cada vocal
    for vocal, conteo in conteo_vocales.items():
        print(f"La vocal '{vocal}' aparece {conteo} veces.")


# Pedir al usuario que ingrese una palabra o frase
frase_usuario = input("Ingresa una palabra o frase: ")
contar_vocales(frase_usuario)
