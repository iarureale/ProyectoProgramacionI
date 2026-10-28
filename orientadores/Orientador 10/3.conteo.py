"""
3. Conteo en una lista. Desarrollar contar_apariciones(datos, buscado) para contar cuántas veces 
aparece un elemento en una lista, sin ciclos ni count(). Ejemplo: [2,4,2,7,2], valor 2 → 3.
"""

def contar_apariciones(datos, buscado):
    if len(datos) == 0:
        return 0
    else:
        cont = 0
        if buscado == datos[0]:
            cont += 1
        return cont + contar_apariciones(datos[1::], 2)

print(contar_apariciones([2,4,2,7,2,2,2], 2))