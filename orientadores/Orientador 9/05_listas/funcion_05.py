"""Contar elementos mayores que un límite."""

def contar_mayores(numeros, limite):
    cantidad = 0
    for numero in numeros:
        if numero > limite:
            cantidad += 1
    return cantidad
