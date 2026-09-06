import funciones


def pedir_opcion_valida(mensaje, opciones_validas):
    """
    Pide un input numérico hasta que sea una de las opciones válidas.
    opciones_validas es una lista de ints, ej: [1, 2, 3]
    """
    opcion = int(input(mensaje))
    while opcion not in opciones_validas:
        print('\nERROR. Ingresar una opción valida.\n')
        opcion = int(input(mensaje))
    return opcion


def menu_principal():
    print("\nBienvenido al OVERPALOOZA!\n")
    print('1. Consultar información del festival \n2. Buscar artista\n3. Consultar grilla \n4. Comprar entradas \n5. Modificar programación\n6. Consultar ventas \n7. Estadísticas e informes\n8. Salir\n')

    opcion = pedir_opcion_valida("Elegir opcion (8 para finalizar): ", [1, 2, 3, 4, 5, 6, 7, 8])

    if opcion == 1:
        consultar_informacion()
    elif opcion == 2:
        buscar_artista()
    elif opcion == 3:
        consultar_grilla()
    elif opcion == 4:
        comprar_entradas()
    elif opcion == 5:
        modificar_programacion()
    elif opcion == 6:
        consultar_venta()
    elif opcion == 7:
        estadisticas()
    elif opcion == 8:
        print('\nGracias por asistir al OVERPALOOZA!\n')


def consultar_informacion():
    print("\nMENU: Consultar información")
    print('\n1. SPONSORS \n2. INGRESO Y APERTURA \n3. OBJETOS NO PERMITIDOS \n4. REDES SOCIALES \n5. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4, 5, 6])
    if opcion == 1:
        print("SPONSORS".center(35, "="))
        print(f"│ {'PRESENTA':<15}: Personal")
        print(f"│ {'MEDIOS DE PAGO':<15}: VISA y Santander")
        print(f"│ {'INVITA':<15}: Fiat")
        print(f"│ {'AUSPICIA':<15}: McDonalds")
        print(f"│ {'PRODUCE':<15}: DfEntertainment\n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        menu_principal()
    elif opcion == 2:
        print("INGRESO Y APERTURA".center(35, "="))
        print("Las puertas del OVERPALOOZA se abrirán a las 11:00AM para el ingreso del público. \n¡Te esperamos!\n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        menu_principal()
    elif opcion == 3:
        print("OBJETOS NO PERMITIDOS".center(35, "="))
        print("\n│🛇  Elementos punzantes \n│🛇  Paraguas \n│🛇  Computadoras \n│🛇  Alcohol \n│🛇  Carteles políticos o religiosos \n│🛇  Alimentos o bebidas \n│🛇  Encendedores \n│🛇  Bengalas \n│🛇  Drones \n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        menu_principal()
    elif opcion == 4:
        print("REDES SOCIALES".center(35, "="))
        print(f"│ {'INSTAGRAM':<15}: overpaloozaar")
        print(f"│ {'FACEBOOK':<15}: overpalooza.ar")
        print(f"│ {'YOUTUBE':<15}: OverpaloozaARG")
        print(f"│ {'TWITTER (X)':<15}: Overpaloozaar \n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        menu_principal()
    elif opcion == 5:
        menu_principal()


def buscar_artista():
    print("\nMENU: Buscar artista")
    print('\n1. Ingresar artista a buscar \n2. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2])

    if opcion == 2:
        menu_principal()


def consultar_grilla():
    print("\nMENU: Consultar grilla")
    print('\n1. Ver lineup\n2. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2])

    if opcion == 1:
        print('\nLINEUP ACTUAL\n')
        funciones.imprimir_grilla(funciones.lineup)
        pedir_opcion_valida("\nPara volver al menu anterior ingresar 1: ", [1])
        consultar_grilla()

    if opcion == 2:
        menu_principal()


def modificar_programacion():
    print("\nMENU: Modificar programación")
    print('\n1. Registrar artista\n2. Asignar artista\n3. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3])

    if opcion == 3:
        menu_principal()


def comprar_entradas():
    print("\nMENU: Comprar entradas")
    print("\n1. Comprar entradas\n2. Chequear disponibilidad\n3. Salir\n")

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3])

    if opcion == 1:
        funciones.tot, funciones.venta_tot = funciones.comprar_entradas(funciones.tot, funciones.venta_tot)
        pedir_opcion_valida("\nIngresar 3 para volver al menu principal: \n", [3])

    elif opcion == 2:
        disponibilidad = funciones.calcular_disponibilidad(funciones.tot, funciones.capacidad_general)
        print(f'\nTodavía queda el {disponibilidad:.2f}% de las entradas\n')
        pedir_opcion_valida("\nIngresar 3 para volver al menu principal: \n", [3])

    menu_principal()


def consultar_venta():
    print("\nMENU: Resumen de ventas")
    porcentaje_vendido = funciones.calcular_porcentaje(funciones.tot, funciones.capacidad_general)
    print(f"\nVentas realizadas: {funciones.tot}\nPorcentaje vendido general: {porcentaje_vendido:.2f}%\n")

    pedir_opcion_valida("Ingresar 1 para volver: ", [1])
    menu_principal()


def estadisticas():
    print("\nMENU: Estadisticas e Informes")
    print("\nEstadisticas:\n")

    pedir_opcion_valida("Ingresar 1 para volver: ", [1])
    menu_principal()