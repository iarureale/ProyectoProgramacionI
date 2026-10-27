"""Identificar números pares."""

def es_par(numero):
    if numero == 0:
        return 0
    return numero % 2 == 0
