def grilla():
    escenarios = 5
    horarios = 8
    lineup = [['.' for c in range(escenarios)] for f in range(horarios)]

    return lineup

def artista_ya_ingresado(artista, lineup):
    """
    Recorre toda la matriz en busca del artista. Retorna true si lo encuentra.
    No se encuentra "while artista in lineup" debido a que chequearia si toda la fila equivale a artista
    """
    for fila in lineup:
        if artista in fila:
            return True
    return False


def ingresar_artista(lineup):
    codigo = input("Ingresar codigo del artista a insertar: ").upper()
    while not validar_codigo(codigo):
        print("ERROR. Ingresé un código válido. ('A-XX')")
        codigo = input("Ingresar codigo del artista a insertar: ").upper()

    while artista_ya_ingresado(codigo, lineup):
        print(f'{codigo} ya esta ingresado en el lineup, Ingresar uno no ingresado')
        artista = input("Ingresar artista a insertar: ").upper()

    nombre_artistico = input("Ingresar nombre del artista ingresado: ")
    horario = int(input("Elegir horario: "))
    escenario = int(input("Ingresar escenario: "))

    while horario < 1 or horario > len(lineup) or escenario < 1 or escenario > len(lineup[0]):
        print(f'Horario o escenario inválido. Horario debe ser entre 1 y {len(lineup)}, escenario entre 1 y {len(lineup[0])}')
        horario = int(input("Elegir horario: "))
        escenario = int(input("Ingresar escenario: "))

    while lineup[horario-1][escenario-1] != '.':
        print(f'El horario {horario} y escenario {escenario} ya tiene un artista asignado')
        horario = int(input("Elegir horario: "))
        escenario = int(input("Ingresar escenario: "))


    lineup[horario-1][escenario-1] = codigo

def imprimir_grilla(lineup, horarios, escenarios):
    """
    Imprime la grilla usando un unico ancho para todas las columnas de
    escenario, calculado automáticamente en base al nombre más largo
    y a los datos cargados. Nos ayuda sin importar qué tan largos sean los nombres, 
    todas las columnas quedan parejas y alineadas.
    """
    margen = 1 

    # Ancho de la columna de horarios
    ancho_horarios = max(len(h) for h in horarios) + margen

    # Ancho único para todas las columnas de escenario:
    ancho = max(len(e) for e in escenarios)
    for f in range(len(lineup)):
        for c in range(len(lineup[f])):
            ancho = max(ancho, len(str(lineup[f][c])))
    ancho += margen

    print(" " * ancho_horarios, end="")
    for i in range(len(escenarios)):
        print(f"|{escenarios[i]:<{ancho}}", end="")
    print("|")

    for f in range(len(lineup)):
        print(f"{horarios[f]:<{ancho_horarios}}|", end="") 
        for c in range(len(lineup[f])):
            print(f"{lineup[f][c]:<{ancho}}|", end="")
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


def calcular_disponibilidad_general(tot, capacidad):
    porcentaje_vendido = calcular_porcentaje(tot, capacidad)
    return 100 - porcentaje_vendido

def validar_codigo(codigo):
    """
    Válida qué el código (str) cumpla con el formato adecuado; "A-XX"
    False: Si no cumple con el formato indicado.
    True: Si cumple con el formato indicado.
    """
    if len(codigo) != 4:
        return False
    if codigo[0:2] != "A-":
        return False
    if not codigo[2::].isdigit():
        return False
    return True


horarios = ['13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00']
escenarios = ['McStage', 'PersonalStage', 'FIATStage', 'FlowStage', 'SantanderStage']

lineup = grilla()
tot = 0
venta_tot = 0
precio = 100000
capacidad_general = 80