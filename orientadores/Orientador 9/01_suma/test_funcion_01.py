from funcion_01 import sumar

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: suma positivos, suma negativos, suma cero.


def test_suma_positivos():
    assert sumar(11,22) == 33

def test_suma_negativos():
    assert sumar(-3,-2) == -5

def test_suma_cero():
    assert sumar(0,0) == 0
