"""Calcular descuentos."""

def precio_final(precio, descuento):
    if precio < 0 or descuento < 0 or descuento > 100:
        return -1
    return precio * (100 - descuento) / 100
