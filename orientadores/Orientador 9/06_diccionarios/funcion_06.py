"""Actualizar stock de un producto."""

def actualizar_stock(stock, producto, cantidad):
    if cantidad < 0:
        return False
    if producto not in stock:
        return False
    stock[producto] += cantidad
    return True
