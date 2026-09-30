import re

texto = "El número de teléfono de Iara es 123-456-7890, y el de Sol es 987-654-3210."
patron = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
nuevoformato = "XXX-XXX-XXXX"
textonuevo = re.sub(patron, nuevoformato, texto)
print("Texto original:")
print(texto)
print("\nTexto con nuevo formato de números de teléfono:")
print(textonuevo)

texto = "Hola, ¿este es el orientador 6? Espero que sea este. Sino sigo buscando."
patron = r"[.,¿? ]+"       
partes = [p for p in re.split(patron, texto) if p] 
print("Partes del texto después de dividir:")
for parte in partes:
    print(parte)


patron = re.compile("[0-9]{4}")
cadena = "07/08/2017|03/02/1984|17/03/1984"

coincidencias = patron.findall(cadena)
print(f"Coincidencias encontradas con findall(): {coincidencias}")

inicio_coincidencia = patron.match(cadena)
print(f"Coincidencia al inicio con match(): {inicio_coincidencia}")   

cadena_reemplazada = patron.sub("XXXX", cadena)
print(f"Cadena después de usar sub(): {cadena_reemplazada}")