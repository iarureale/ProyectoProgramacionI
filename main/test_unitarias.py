from funciones import *

def test_codigo_invalido(): # Validaciónes incorrectas.
    assert validar_codigo("B-01") == False
    assert validar_codigo("A-1") == False

def test_codigo_valido(): # Validación correcta.
    assert validar_codigo("A-01") == True

#------------

def test_calcular_disponibilidad(): # Cálculo simple con resultado conocido.
    assert calcular_disponibilidad_general(5, 10) == 50

#------------

# Pruebas de casos límite

def test_es_cantidad_invalida():
    assert es_cantidad_valida("0") == False

def test_es_cantidad_valida():
    assert es_cantidad_valida("1") == True

#------------

def test_general_sin_stock(): # Detección de condición crítica: stock restante de entradas generales (0); devuelve 0.
    entradas = {
        "General": {"precio": 100000, "cupo_maximo": 80, "max_operacion": 6},
        "VIP":     {"precio": 250000, "cupo_maximo": 20, "max_operacion": 6},
    }
    assert calcular_limite_compra(1, entradas, 80, 20) == 0 

def test_vip_sin_stock(): # Detección de condición crítica: stock restante de entradas vip (0) ; devuelve 0.
    entradas = {
        "General": {"precio": 100000, "cupo_maximo": 80, "max_operacion": 6},
        "VIP":     {"precio": 250000, "cupo_maximo": 20, "max_operacion": 6},
    }
    assert calcular_limite_compra(2, entradas, 80, 20) == 0 

#------------

def test_disponibilidad_capacidad_cero(): # Validación incorrecta que produce una excepción.
    try:
        calcular_disponibilidad_general(5, 0)
        assert False
    except ZeroDivisionError:
        assert True

#------------

def test_contar_artistas_por_escenario(): # Acumulación por clave (escenario).
    escenarios = ("McStage", "PStage", "FIATStage", "FlowStage", "SanStage")
    lineup = grilla()
    lineup[0][0] = "A-01"
    lineup[1][0] = "A-02"
    lineup[0][2] = "A-03"
    assert contar_artistas_escenario(lineup, escenarios) == [2, 0, 1, 0, 0]