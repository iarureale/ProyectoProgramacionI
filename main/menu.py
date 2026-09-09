import funciones


def pedir_opcion_valida(mensaje, opciones_validas):
    '''
    Pide un input numérico hasta que sea una de las opciones válidas.
    opciones_validas es una lista de ints, ej: [1, 2, 3]
   '''
    opcion = input(mensaje)

    while not opcion.isdigit() or int(opcion) not in opciones_validas:
        print('\nERROR. Ingresar una opción valida.')
        opcion = input(mensaje)

    return int(opcion)


def menu_principal():
    horarios = ('13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00')
    escenarios = ('McStage', 'PStage', 'FIATStage', 'FlowStage', 'SanStage')

    codigos = []
    nombre_artistas = []


    lineup = funciones.grilla()
    tot = 0
    venta_tot = 0


    general = (100000, 80) 
    vip = (250000, 20) 
    entradas = [general, vip] 

    vendidas_gen = 0
    vendidas_vip = 0

    capacidad_general = general[1] + vip[1]
    print("\nBienvenido al OVERPALOOZA!\n")
    print('1. Consultar información del festival \n2. Buscar artista\n3. Consultar grilla \n4. Comprar entradas \n5. Modificar programación\n6. Consultar ventas \n7. Estadísticas e informes\n8. Salir\n')

    opcion = pedir_opcion_valida("Elegir opcion (8 para finalizar): ", [1, 2, 3, 4, 5, 6, 7, 8])

    if opcion == 1:
        consultar_informacion()
    elif opcion == 2:
        buscar_artista()
    elif opcion == 3:
        consultar_grilla(lineup, horarios, escenarios)
    elif opcion == 4:
        menu_comprar_entradas(tot, venta_tot, entradas, vendidas_vip, vendidas_gen, capacidad_general)
    elif opcion == 5:
        modificar_programacion(lineup, nombre_artistas, codigos)
    elif opcion == 6:
        consultar_venta(tot, capacidad_general)
    elif opcion == 7:
        estadisticas()
    elif opcion == 8:
        print("="*60)
        print('Gracias por asistir al OVERPALOOZA!'.center(60, '-'))
        print("="*60)


def consultar_informacion():
    print("\nMENU: Consultar información")
    print('\n1. SPONSORS \n2. INGRESO Y APERTURA \n3. OBJETOS NO PERMITIDOS \n4. REDES SOCIALES \n5. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4, 5, 6])
    if opcion == 1:
        print("SPONSORS".center(35, "="))
        print(f"│ {'PRESENTA':<15}: Personal y FLOW")
        print(f"│ {'MEDIOS DE PAGO':<15}: VISA y Santander")
        print(f"│ {'INVITA':<15}: Fiat")
        print(f"│ {'AUSPICIA':<15}: McDonalds")
        print(f"│ {'PRODUCE':<15}: DfEntertainment\n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion()
    elif opcion == 2:
        print("INGRESO Y APERTURA".center(35, "="))
        print("Las puertas del OVERPALOOZA se abrirán a las 11:00AM para el ingreso del público. \n¡Te esperamos!\n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion()
    elif opcion == 3:
        print("OBJETOS NO PERMITIDOS".center(35, "="))
        print("\n│🛇  Elementos punzantes \n│🛇  Paraguas \n│🛇  Computadoras \n│🛇  Alcohol \n│🛇  Carteles políticos o religiosos \n│🛇  Alimentos o bebidas \n│🛇  Encendedores \n│🛇  Bengalas \n│🛇  Drones \n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion()
    elif opcion == 4:
        print("REDES SOCIALES".center(35, "="))
        print(f"│ {'INSTAGRAM':<15}: overpaloozaar")
        print(f"│ {'FACEBOOK':<15}: overpalooza.ar")
        print(f"│ {'YOUTUBE':<15}: OverpaloozaARG")
        print(f"│ {'TWITTER (X)':<15}: Overpaloozaar \n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion()
    elif opcion == 5:
        menu_principal()


def buscar_artista():
    print("\nMENU: Buscar artista")
    print('\n1. Ingresar artista a buscar \n2. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2])

    if opcion == 2:
        menu_principal()


def consultar_grilla(lineup, horarios, escenarios):
    print("\nMENU: Consultar grilla")
    print('\n1. Ver lineup\n2. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2])

    if opcion == 1:
        print('\nLINEUP ACTUAL\n')
        funciones.imprimir_grilla(lineup, horarios, escenarios)
        pedir_opcion_valida("\nPara volver al menu anterior ingresar 1: ", [1])
        consultar_grilla(lineup, horarios, escenarios)

    if opcion == 2:
        menu_principal()


def modificar_programacion(lineup, nombre_artistas, codigos):
    print("\nMENU: Modificar programación")
    print('\n1. Registrar artista\n2. Asignar artista\n3. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3])
    registrados = 0

    if opcion == 1:
        print("MENU: Registrar artista")
        while registrados < 30:
            funciones.ingresar_artista(lineup, nombre_artistas, codigos)
            registrados +=1
            print("\nSi se quiere parar de ingresar porfavor ingresar 3 de lo contrario 1")
            opcion = pedir_opcion_valida('Ingresar:', [1, 3])
            if opcion == 3:
                modificar_programacion(lineup, nombre_artistas, codigos)
    elif opcion == 2:
        print("MENU: Modificar artista\n")
        if not codigos:
            print("No se ha registrado ningun artista todavía.\n")
            pedir_opcion_valida("Volver al menu principal (1)", [1])
            modificar_programacion(lineup, nombre_artistas, codigos)
            return
        for i in range(len(codigos)):
            print(f'Artista {i+1}: {codigos[i]} - {nombre_artistas[i]}\n')
        #FUNCION NUEVA
        modificar_artista = input("Ingresar codigo del artista a modificar: ").upper()
        while not funciones.validar_codigo(modificar_artista):
            print("ERROR. Ingresé un código válido. ('A-XX')")
            modificar_artista = input("Ingresar codigo del artista a modificar: ").upper()

        indice = codigos.index(modificar_artista)
        print('Ingresar numero del dato a modificar:\n1.Cambiar nombre del artista\n2.Cambiar horario\n3.Cambiar escenario')

        modificar_datos = pedir_opcion_valida("Ingresar: ", [1, 2, 3])
        if modificar_datos == 1:
            nombre = input("Ingresar el nombre nuevo: ")
            nombre_artistas[indice] = nombre
            print(f"El artista {codigos[indice]} ha pasado a ser {nombre}")
            

        


    if opcion == 3:
        menu_principal()


def menu_comprar_entradas(tot, venta_tot, entradas, vendidas_vip, vendidas_gen, capacidad_general):
    print("\nMENU: Comprar entradas")
    print("\n1. Comprar entradas\n2. Chequear disponibilidad\n3. Salir\n")

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3])

    if opcion == 1:
        print("\nMENU: Comprar entradas")
        print(f'\nGeneral: ${entradas[0][0]} \nVIP: ${entradas[1][0]}')
        print("\nQue tipo de entradas queres comprar?")
        print("1. General\n2. VIP\n")

        tipo = pedir_opcion_valida("Ingresar: ", [1, 2])

        if tipo == 1:
            tot, venta_tot, = funciones.comprar_entradas(tot, venta_tot, entradas, vendidas_vip, vendidas_gen, capacidad_general)
            print("TU COMPRA HA SIDO EXITOSA!".center(40, '='))
            pedir_opcion_valida("\nIngresar 1 para volver al menu principal: \n", [1])
            menu_comprar_entradas(tot, venta_tot, entradas, vendidas_vip, vendidas_gen, capacidad_general)
        elif tipo == 2:
            tot, venta_tot, = funciones.comprar_entradas(tot, venta_tot, entradas, vendidas_vip, vendidas_gen, capacidad_general)
            print("TU COMPRA HA SIDO EXITOSA!".center(40, '='))
            pedir_opcion_valida("\nIngresar 1 para volver al menu principal: \n", [1])
            menu_comprar_entradas(tot, venta_tot, entradas, vendidas_vip, vendidas_gen, capacidad_general)
        
    elif opcion == 2:
        disponibilidad = funciones.calcular_disponibilidad_general(tot, capacidad_general)
        print(f'\nTodavía queda el {disponibilidad:.2f}% de las entradas generales\n')
        pedir_opcion_valida("\nIngresar 3 para volver al menu principal: \n", [3])

    menu_principal()


def consultar_venta(tot, capacidad_general):
    print("\nMENU: Resumen de ventas")
    porcentaje_vendido = funciones.calcular_porcentaje(tot, capacidad_general)
    print(f"\nVentas realizadas: {tot}\nPorcentaje vendido general: {porcentaje_vendido:.2f}%\n")

    pedir_opcion_valida("Ingresar 1 para volver: ", [1])
    menu_principal()


def estadisticas():
    print("\nMENU: Estadisticas e Informes")
    print("\nEstadisticas:\n")

    pedir_opcion_valida("Ingresar 1 para volver: ", [1])
    menu_principal()