from funcion_06 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: producto existente, producto inexistente, cantidad negativa.

def test_producto_existente():
    stock = {"medias": 4,
             "corbata": 4,
             "celular": 2,}
    assert actualizar_stock(stock, "medias", 1) == True
    
def test_producto_inexistente():
    stock = {"medias": 4,
         "corbata": 4,
         "celular": 2,}
    assert actualizar_stock(stock, "hola", 1) == False

def test_cantidad_negativa():
    stock = {"medias": 4,
             "corbata": 4,
             "celular": 2,}
    assert actualizar_stock(stock, "medias", -2) == False

