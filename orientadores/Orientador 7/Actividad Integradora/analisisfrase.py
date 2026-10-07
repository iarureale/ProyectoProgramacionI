frase = input("Ingrese una frase: ")

# a) Normalizar a minúsculas
frase = frase.lower()

# b) Eliminar signos de puntuación
signos = [".", ",", ";", ":", "?", "¿", "!", "¡"]
for signo in signos:
    frase = frase.replace(signo, "")

# c) Separar en palabras
palabras = frase.split()

# d) Conjunto con las palabras diferentes
unicas = set(palabras)

# e) Diccionario de frecuencias
frecuencias = {}
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

# h) Solo si se ingresó al menos una palabra
if len(palabras) == 0:
    print("No se ingresaron palabras.")
else:
    # f) Palabras sin repetir en orden alfabético
    print("\nPalabras sin repetir (orden alfabético):")
    for palabra in sorted(unicas):
        print("-", palabra)

    # g) Cada palabra con su frecuencia
    print("\nFrecuencia de cada palabra:")
    for palabra in sorted(frecuencias):
        print(palabra, "aparece", frecuencias[palabra], "veces")

    # h) Palabra más frecuente
    mas_frecuente = max(frecuencias, key=frecuencias.get)
    print("\nPalabra más frecuente:", mas_frecuente,
          "(", frecuencias[mas_frecuente], "veces )")