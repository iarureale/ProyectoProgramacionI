frase = input("Lenguajes: ")
palabras = frase.split()
unicos = set(palabras)
conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(unicos)
for clave in sorted(conteo):
    print(clave, conteo[clave])

#Reverse: true para ordenar de menor a mayor