from funcion_05 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: varios mayores, ninguno, lista vacia, igual no cuenta.

def test_varios_mayores():
    assert contar_mayores([1,5,2,6], 3) == 2

def test_ninguno():
    assert contar_mayores([1,2,3,4], 5) == 0

def test_lista_vacia():
    assert contar_mayores([], 3) == 0

def test_igual_no_cuenta():
    assert contar_mayores([3,5,6,3], 3) == 2
