def grilla():
    escenarios = 5
    horarios = 8
    lineup = [['.' for c in range(escenarios)] for f in range(horarios)]

    return lineup


def ingresar_artista(lineup):
    artista = input("Ingresar artista a insertar: ")
    horario = int(input("Elegir horario: "))
    escenario = int(input("Ingresar escenario: "))

    lineup[horario-1][escenario-1] = artista


def imprimir_grilla(lineup):
    ancho = 12
    for f in range(len(lineup)):
        for c in range(len(lineup[f])):
            print(f"{lineup[f][c]:<{ancho}}", end="")
        print()


def comprar_entradas(tot, venta_tot):
    print("\nIngresar entradas a comprar:\n")

    entradas = int(input())
    while entradas > 5:
        print('\nLa cantidad ingresada supera la permitida por compra. Se permiten 5 por usuario\n')
        entradas = int(input('Ingresar entradas a comprar: '))

    tot += entradas
    venta_tot += entradas * precio
    return tot, venta_tot


def calcular_porcentaje(tot, capacidad):
    porcentaje = (tot / capacidad) * 100
    return porcentaje


def calcular_disponibilidad(tot, capacidad):
    porcentaje_vendido = calcular_porcentaje(tot, capacidad)
    return 100 - porcentaje_vendido


tot = 0
venta_tot = 0
precio = 100000
capacidad_general = 80