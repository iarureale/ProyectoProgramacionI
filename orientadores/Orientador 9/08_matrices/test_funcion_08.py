from funcion_08 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: matriz dos filas, matriz vacia, valores negativos, una fila.

def test_matriz_dos_filas():
    assert sumar_matriz([[1,2,3],[4,5,6]]) == 21

def test_matriz_vacia():
    assert sumar_matriz([[],[]]) == 0

def test_valores_negativos():
    assert sumar_matriz([[-1,-2,-3],[-4,-5,-6]]) == -21
def test_una_fila():
    assert sumar_matriz([[3]]) == 3
