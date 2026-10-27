from funcion_09 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: dos productos, producto repetido, sin ventas, venta cero.

def test_dos_productos():
    ventas = {("manzana", 4,1000), ("naranja", 5, 100)}
    assert resumen_ventas(ventas) == {"manzana": 4000, "naranja": 500}

def test_producto_repetido():
    ventas = {("manzana", 4,1000), ("manzana", 5, 100)}
    assert resumen_ventas(ventas) == {"manzana": 4500}

def test_sin_ventas():
    ventas = {}
    assert resumen_ventas(ventas) == {}

def test_venta_cero():
    ventas = {("manzana", 0,1000), ("naranja", 0, 100)}
    assert resumen_ventas(ventas) == {"manzana": 0, "naranja": 0}