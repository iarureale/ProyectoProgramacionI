"""Resumir ventas por producto."""

def resumen_ventas(ventas):
    resumen = {}
    for producto, unidades, precio in ventas:
        if producto not in resumen:
            resumen[producto] = 0
        resumen[producto] += unidades * precio
    return resumen

