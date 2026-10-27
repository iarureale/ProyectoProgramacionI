from funcion_02 import es_par

# CONSIGNA: escribir pruebas usando solo assert.
# Casos sugeridos: numero par, numero impar, cero.

def test_numero_par():
    assert es_par(2) == True

def test_numero_impar():
    assert es_par(3) == False

def test_cero():
    assert es_par(0) == 0
