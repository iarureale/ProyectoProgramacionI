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


def menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip):
    horarios = ('13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00')
    escenarios = ('McStage', 'PStage', 'FIATStage', 'FlowStage', 'SanStage')

    general = (100000, 80) 
    vip = (250000, 20) 
    entradas = [general, vip] 

    capacidad_general = general[1] + vip[1]

    max_operacion = 6

    print("\nBienvenido al OVERPALOOZA!\n")
    print('1. Consultar información del festival \n2. Buscar artista\n3. Consultar grilla \n4. Comprar entradas \n5. Modificar programación\n6. Consultar ventas \n7. Estadísticas e informes\n8. Salir\n')

    opcion = pedir_opcion_valida("Elegir opcion (8 para finalizar): ", [1, 2, 3, 4, 5, 6, 7, 8])

    if opcion == 1:
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)
    elif opcion == 2:
        menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios)
    elif opcion == 3:
        consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)
    elif opcion == 4:
        menu_comprar_entradas(tot, venta_tot, entradas, vendidas_vip, vendidas_gen, capacidad_general, max_operacion, lineup, nombre_artistas, codigos)
    elif opcion == 5:
        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios)
    elif opcion == 6:
        consultar_venta(tot, capacidad_general, lineup, nombre_artistas, codigos, venta_tot, vendidas_gen, vendidas_vip)
    elif opcion == 7:
        estadisticas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, capacidad_general, entradas)
    elif opcion == 8:
        print("="*60)
        print('Gracias por asistir al OVERPALOOZA!'.center(60, '-'))
        print("="*60)


def consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip):
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
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)
    elif opcion == 2:
        print("INGRESO Y APERTURA".center(35, "="))
        print("Las puertas del OVERPALOOZA se abrirán a las 11:00AM para el ingreso del público. \n¡Te esperamos!\n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)
    elif opcion == 3:
        print("OBJETOS NO PERMITIDOS".center(35, "="))
        print("\n│🛇  Elementos punzantes \n│🛇  Paraguas \n│🛇  Computadoras \n│🛇  Alcohol \n│🛇  Carteles políticos o religiosos \n│🛇  Alimentos o bebidas \n│🛇  Encendedores \n│🛇  Bengalas \n│🛇  Drones \n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)
    elif opcion == 4:
        print("REDES SOCIALES".center(35, "="))
        print(f"│ {'INSTAGRAM':<15}: overpaloozaar")
        print(f"│ {'FACEBOOK':<15}: overpalooza.ar")
        print(f"│ {'YOUTUBE':<15}: OverpaloozaARG")
        print(f"│ {'TWITTER (X)':<15}: Overpaloozaar \n")
        opcion = pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)
    elif opcion == 5:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)


def menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios):
    print("\nMENU: Buscar artista\n")
    print('\n1. Ingresar artista a buscar \n2. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2])

    if opcion == 1:
        buscado = (input("\nIngresar código o nombre del artista a buscar, (2) para salir: ")).strip().lower()

        if buscado == "2":
            menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios)

        else:
            while buscado not in [n.lower() for n in nombre_artistas] and buscado not in [c.lower() for c in codigos] and buscado != "2":
                print("ERROR. ingresar un código o nombre válido.")
                opcion_a = pedir_opcion_valida("(1) Para intentarlo nuevamente, (2) para salir: ", [1, 2])

                if opcion_a == 1:
                    buscado = (input("\nIngresar código o nombre del artista a buscar: ")).strip().lower()
                else:
                    buscado = "2"

            if buscado == "2":
                menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios)
            else:
                nombre, escenario, horario = funciones.buscar_artista(buscado, codigos, nombre_artistas, lineup, escenarios, horarios)

                if escenario != ".":
                    print(f"\nArtista: {nombre}")
                    print(f"Escenario: {escenario}")
                    print(f"Horario: {horario}")
                else:
                    print(f"\nEl artista {nombre} todavía no tiene ni escenario ni horario asignado.")

                pedir_opcion_valida("\nIngresar 1 para volver al menú anterior:", [1])
                menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios)

    else:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)

def consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip):
    print("\nMENU: Consultar grilla")
    print('\n1. Ver lineup\n2. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2])

    if opcion == 1:
        print('\nLINEUP ACTUAL\n')

        print("\nLINEUP POR CODIGO\n")
        funciones.imprimir_grilla(lineup, horarios, escenarios)
        print('\n\n')

        print('=' * 63)

        print("\n\nLINEUP POR NOMBRE\n")

        funciones.imprimir_grilla_con_nombres(lineup, horarios, escenarios, codigos, nombre_artistas)


        pedir_opcion_valida("\nPara volver al menu anterior ingresar 1: ", [1])
        consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)

    if opcion == 2:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)


def modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios):
    print("\nMENU: Modificar programación")
    print('\n1. Registrar artista\n2. Modificar artista\n3. Salir\n')

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3])
    registrados = 0

    if opcion == 1:
        print("MENU: Registrar artista")
        while registrados < 30:
            funciones.ingresar_artista(lineup, nombre_artistas, codigos)
            registrados +=1
            print("\nSi se quiere parar de ingresar porfavor ingresar 3 de lo contrario 1")
            volver = pedir_opcion_valida('Ingresar:', [1, 3])

            if volver == 3:
                modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios)
                return
    elif opcion == 2:
        print("MENU: Modificar artista\n")
        if not codigos:
            print("No se ha registrado ningun artista todavía.\n")
            pedir_opcion_valida("Volver al menu principal (1)", [1])
            modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios)
            return
        for i in range(len(codigos)):
            print(f'Artista {i+1}: {codigos[i]} - {nombre_artistas[i]}\n')
        modificar_artista = input("Ingresar codigo del artista a modificar: ").upper()
        while not funciones.validar_codigo(modificar_artista):
            print("ERROR. Ingresé un código válido. ('A-XX')")
            modificar_artista = input("Ingresar codigo del artista a modificar: ").upper()

        indice = codigos.index(modificar_artista)
        print('Ingresar numero del dato a modificar:\n1.Modificar codigo del artista\n2.Cambiar nombre del artista\n3.Cambiar horario\n4.Cambiar escenario')

        modificar_datos = pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4])
        if modificar_datos == 1:
            codigo_nuevo = (input("Ingresar codigo nuevo: ")).upper()
            while not funciones.validar_codigo(codigo_nuevo) or funciones.artista_ya_ingresado(codigo_nuevo, codigos):
                if not funciones.validar_codigo(codigo_nuevo):
                    print("ERROR. Ingresé un código válido. ('A-XX')")
                else:
                    print(f"ERROR. El código {codigo_nuevo} ya está en uso por otro artista.")
                codigo_nuevo = input("Ingresar codigo nuevo: ").upper()
            funciones.cambiar_artista(lineup, codigos, indice, codigo_nuevo)
            print(f"El/La artista {nombre_artistas[indice]} ha pasado a ser {codigo_nuevo}")

            volver = pedir_opcion_valida("Volver al menu anterior (1): ", [1])
            if volver == 1:
                modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios)

        elif modificar_datos == 2:
            nombre = input("Ingresar el nombre nuevo: ")
            nombre_artistas[indice] = nombre
            print(f"El artista {codigos[indice]} ha pasado a ser {nombre}")
            volver =pedir_opcion_valida("Volver al menu anterior (1): ", [1])
            if volver == 1:
                modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios)
        elif modificar_datos == 3:
            horario_viejo, escenario_viejo = funciones.buscar_posicion_en_lineup(lineup, modificar_artista)

            horario_nuevo = pedir_opcion_valida("Ingresar el horario nuevo: ", [1, 2, 3, 4, 5, 6, 7, 8])
            horario_nuevo = funciones.validar_horario(horario_nuevo, lineup, escenario_viejo)

            lineup[horario_viejo-1][escenario_viejo-1] = '.'
            lineup[horario_nuevo-1][escenario_viejo-1] = modificar_artista
            print(f"El artista {modificar_artista} ha sido movido al horario {horario_nuevo}.")

            volver = pedir_opcion_valida("Volver al menu anterior (1): ", [1])
            if volver == 1:
                modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios)
        elif modificar_datos == 4:
            horario_viejo, escenario_viejo = funciones.buscar_posicion_en_lineup(lineup, modificar_artista)
        
            escenario_nuevo = pedir_opcion_valida("Ingresar el escenario nuevo: ", [1, 2, 3, 4, 5])
            escenario_nuevo = funciones.validar_escenario(escenario_nuevo, lineup, horario_viejo)
        
            lineup[horario_viejo-1][escenario_viejo-1] = '.'
            lineup[horario_viejo-1][escenario_nuevo-1] = modificar_artista
            print(f"El artista {modificar_artista} ha sido movido al escenario {escenario_nuevo}.")
        
            volver = pedir_opcion_valida("Volver al menu anterior (1): ", [1])
            if volver == 1:
                modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios)
          
  
    elif opcion == 3:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)


def menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos):
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
            tot, venta_tot, vendidas_gen, vendidas_vip = funciones.comprar_entradas(tot, venta_tot, entradas, tipo, vendidas_gen, vendidas_vip, max_operacion)
            print("TU COMPRA HA SIDO EXITOSA!".center(40, '='))
            pedir_opcion_valida("\nIngresar 1 para volver al menu principal: \n", [1])
            menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos)
        elif tipo == 2:
            tot, venta_tot, vendidas_gen, vendidas_vip = funciones.comprar_entradas(tot, venta_tot, entradas, tipo, vendidas_gen, vendidas_vip, max_operacion)
            print("TU COMPRA HA SIDO EXITOSA!".center(40, '='))
            pedir_opcion_valida("\nIngresar 1 para volver al menu principal: \n", [1])
            menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos)
        
    elif opcion == 2:
        disponibilidad = funciones.calcular_disponibilidad_general(tot, capacidad_general)
        print(f'\nTodavía queda el {disponibilidad:.2f}% de las entradas generales\n')
        pedir_opcion_valida("\nIngresar 3 para volver al menu principal: \n", [3])

    menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)


def consultar_venta(tot, capacidad_general, lineup, nombre_artistas, codigos, venta_tot, vendidas_gen, vendidas_vip):
    print("\nMENU: Resumen de ventas")
    porcentaje_disponibilidad = funciones.calcular_disponibilidad_general(tot, capacidad_general)
    porcentaje_vendido = 100 - porcentaje_disponibilidad

    print(f"\nVentas realizadas: {tot}\nPorcentaje vendido general: {porcentaje_vendido:.2f}%\n")

    volver = pedir_opcion_valida("Ingresar 1 para volver: ", [1])
    if volver == 1:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)

def estadisticas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, capacidad_general, entradas):
    print("\n1. Ranking mejores escenarios por votación\n2. Información de entradas\n3. Recaudación total\n4. Porcentaje de ocupación\n5. Salir\n")

    opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4, 5])

    if opcion == 1:
        print("Los mejores escenarios por votación fueron:")
    elif opcion == 2:
        precio_general = entradas[0][0]
        precio_vip = entradas[1][0]
        rec_gen = vendidas_gen * precio_general
        rec_vip = vendidas_vip * precio_vip
        print(f"General vendidas: {vendidas_gen}\nRecaudación General: ${rec_gen}")
        print(f'VIP vendidas: {vendidas_vip}\nRecaudación VIP: ${rec_vip}\n')
    elif opcion == 3:
        print(f"Recaudación total: ${venta_tot}")
    elif opcion == 4:
        porcentaje = 100 - funciones.calcular_disponibilidad_general(vendidas_gen + vendidas_vip, capacidad_general)
        print(f"Porcentaje de ocupación: {porcentaje:.2f}%")
    elif opcion == 5:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip)
        return

    volver = pedir_opcion_valida("\nIngresar 1 para volver al menu principal: ", [1])
    if volver == 1:
        estadisticas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, capacidad_general, entradas)
   
    