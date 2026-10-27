from funcion_04 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: mayusculas, espacios, vacio.

def test_mayusculas():
    assert normalizar("HOLA") == "hola"

def test_espacios():
    assert normalizar(" buen dia ") == "buen dia"

def test_vacio():
    assert normalizar("") == ""
