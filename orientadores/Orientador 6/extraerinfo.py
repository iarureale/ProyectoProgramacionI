import re

texto = ("Contacto de Iara: iara@dominio.com, tel 1234-5678, producto AB1234. "
         "Contacto de Sol: sol@dominio.com, tel 4321-8765, producto CD5678. "
         "Datos que no deben coincidir: ab1234, 12345678, oliver@, 123-4567, A12345.")

correo = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
telefono = r'\b[0-9]{4}-[0-9]{4}\b'
codigo = r'\b[A-Z]{2}[0-9]{4}\b'

tipos = [("correos electrónicos", correo),
         ("teléfonos", telefono),
         ("códigos de producto", codigo)]

print("Texto de prueba:")
print(texto)


for nombre, patron in tipos:
    coincidencias = re.findall(patron, texto)
    if coincidencias:
        print(f"Coincidencias de {nombre}: {coincidencias}")
        print(f"Cantidad de {nombre}: {len(coincidencias)}")
    else:
        print(f"No se encontraron {nombre}.")
    print()


for nombre, patron in tipos:
    print(f"Información detallada de {nombre}:")
    iterador = re.finditer(patron, texto)
    for match in iterador:
        print(f"Encontrado: {match.group()}")
        print(f"Ubicación: inicio={match.start()}, fin={match.end()}")
        

patron = '[A-Z]{2}[0-9]{4}'
cadena = "XYZAB12345"
print(f'findall con "{patron}" sobre "{cadena}": {re.findall(patron, cadena)}')
if re.fullmatch(patron, cadena):
    print(f'La cadena "{cadena}" coincide con el patrón completo.')
else:
    print(f'La cadena "{cadena}" no coincide con el patrón completo.')