palabra = "Hola mundo Python"

# Convertir la palabra a minúsculas para contar tanto vocales mayúsculas como minúsculas
palabra = palabra.lower()

# Inicializar un diccionario para almacenar la cantidad de cada vocal
contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Contar las vocales y actualizar el diccionario
for letra in palabra:
    if letra in contador_vocales:
        contador_vocales[letra] += 1

# Imprimir el resultado
for vocal, cantidad in contador_vocales.items():
    print(f"La cantidad de '{vocal}' es: {cantidad}")
