from funcion_07 import *

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: clave valida, clave corta, sin numeros, limite ocho.

def test_clave_valida():
    assert clave_valida("hola1234") == True

def test_clave_corta():
    assert clave_valida("1234") == False

def test_sin_numeros():
    assert clave_valida("holaholahola") == False

def test_limite_ocho():
    assert clave_valida("12345678") == True
