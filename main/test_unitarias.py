from funciones import *

def test_repetido():
    assert repitencia_usuarios("admin", "admin@gmail.com") == True

def test_no_repetido(): #Validación correcta
    assert repitencia_usuarios("juan", "juan123@gmail.com") == False

#------------

def test_calcular_disponibilidad(): # Cálculo simple con resultado conocido
    assert calcular_disponibilidad_general(5, 10) == 50

# Casos límite
def test_es_cantidad_valida():
    assert es_cantidad_valida("0") == False

def test_es_cantidad_invalida():
    assert es_cantidad_valida("1") == True