"""Sumar una matriz rectangular."""

def sumar_matriz(matriz):
    total = 0
    for fila in matriz:
        for valor in fila:
            total += valor
    return total
