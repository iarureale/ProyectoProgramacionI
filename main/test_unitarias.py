from funciones import *

def test_repetido():
    assert repitencia_usuarios("admin", "admin@gmail.com") == True

def test_no_repetido(): #Validación correcta
    assert repitencia_usuarios("juan", "juan123@gmail.com") == False

#------------

def test_calcular_disponibilidad():
    assert calcular_disponibilidad_general(5, 10) == 50

