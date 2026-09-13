import funciones

def menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados):
    """
    Recibe la matriz lineup, las listas de artistas y codigos, y los acumuladores de venta.
    No retorna un valor, muestra el menu principal del sistema y llama a las funciones correspondientes según la opción elegida por el usuario.
    """
    horarios = ('13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00')
    escenarios = ('McStage', 'PStage', 'FIATStage', 'FlowStage', 'SanStage')

    general = (100000, 80) 
    vip = (250000, 20) 
    entradas = [general, vip] 

    capacidad_general = general[1] + vip[1] # Entradas en total (80 + 20 = 100)

    max_operacion = 6

    print("\nBienvenido al OVERPALOOZA!\n")
    print('1. Consultar información del festival \n2. Buscar artista\n3. Consultar grilla \n4. Comprar entradas \n5. Modificar programación\n6. Estadísticas e informes\n7. Salir\n')

    opcion = funciones.pedir_opcion_valida("Elegir opcion (7 para finalizar): ", [1, 2, 3, 4, 5, 6, 7])

    if opcion == 1:
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    elif opcion == 2:
        menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios, escenarios_rankeados)
    elif opcion == 3:
        consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    elif opcion == 4:
        menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos, general, vip, escenarios_rankeados, escenarios)
    elif opcion == 5:
        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
    elif opcion == 6:
        estadisticas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, capacidad_general, entradas, escenarios_rankeados)
    elif opcion == 7:
        print("="*60)
        print('Gracias por asistir al OVERPALOOZA!'.center(60, '-'))
        print("="*60)

def consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados):
    """
    Recibe la matriz lineup, las listas de artistas y codigos, y los acumuladores de venta.
    No retorna un valor, muestra el submenú de información general del festival y la informacion correspondiente a la opción elegida por el usuario.
    """
    print("\nMENÚ: Consultar información")
    print('\n1. SPONSORS \n2. INGRESO Y APERTURA \n3. OBJETOS NO PERMITIDOS \n4. REDES SOCIALES \n5. Salir\n')

    opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4, 5])
    if opcion == 1:
        print("SPONSORS".center(35, "="))
        print(f"│ {'PRESENTA':<15}: Personal y FLOW")
        print(f"│ {'MEDIOS DE PAGO':<15}: VISA y Santander")
        print(f"│ {'INVITA':<15}: Fiat")
        print(f"│ {'AUSPICIA':<15}: McDonalds")
        print(f"│ {'PRODUCE':<15}: DfEntertainment\n")
        opcion = funciones.pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    elif opcion == 2:
        print("INGRESO Y APERTURA".center(35, "="))
        print("Las puertas del OVERPALOOZA se abrirán a las 11:00AM para el ingreso del público. \n¡Te esperamos!\n")
        opcion = funciones.pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    elif opcion == 3:
        print("OBJETOS NO PERMITIDOS".center(35, "="))
        print("\n│🛇  Elementos punzantes \n│🛇  Paraguas \n│🛇  Computadoras \n│🛇  Alcohol \n│🛇  Carteles políticos o religiosos \n│🛇  Alimentos o bebidas \n│🛇  Encendedores \n│🛇  Bengalas \n│🛇  Drones \n")
        opcion = funciones.pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    elif opcion == 4:
        print("REDES SOCIALES".center(35, "="))
        print(f"│ {'INSTAGRAM':<15}: overpaloozaar")
        print(f"│ {'FACEBOOK':<15}: overpalooza.ar")
        print(f"│ {'YOUTUBE':<15}: OverpaloozaARG")
        print(f"│ {'TWITTER (X)':<15}: Overpaloozaar \n")
        opcion = funciones.pedir_opcion_valida("Ingrese (1) para volver al menú principal: ", [1])
        consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    elif opcion == 5:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

def menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios, escenarios_rankeados):
    """
    Recibe la matriz lineup, las listas de artistas y codigos, los acumuladores de venta y las tuplas de escenarios y horarios.
    No retorna un valor; permite buscar un artista por código o nombre, mostrando su información correspondiente, y permite volver al menú principal.
    """
    print("\nMENÚ: Buscar artista\n")
    if codigos:
        print('\n1. Ingresar artista a buscar \n2. Salir\n')
        opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2])
        funciones.imprimir_artistas_ordenados(nombre_artistas)
        if opcion == 1:
            buscado = (input("\nIngresar código o nombre del artista a buscar, o (2) para salir: ")).strip().lower()

            if buscado == "2":
                menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios, escenarios_rankeados)

            else:
                while buscado not in [n.lower() for n in nombre_artistas] and buscado not in [c.lower() for c in codigos] and buscado != "2":
                    print("[ERROR] Ingrese un código o nombre válido.")
                    opcion_a = funciones.pedir_opcion_valida("(1) Para intentarlo nuevamente, (2) para salir: ", [1, 2])

                    if opcion_a == 1:
                        buscado = (input("\nIngresar código o nombre del artista a buscar: ")).strip().lower()
                    else:
                        buscado = "2"

                if buscado == "2":
                    menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios, escenarios_rankeados)
                else:
                    nombre, escenario, horario = funciones.buscar_artista(buscado, codigos, nombre_artistas, lineup, escenarios, horarios)

                    if escenario != ".":
                        print(f"\nArtista: {nombre}")
                        print(f"Escenario: {escenario}")
                        print(f"Horario: {horario}")

                    funciones.pedir_opcion_valida("\nIngresar (1) para volver al menú anterior: ", [1])
                    menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios, escenarios_rankeados)

        else:
            menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    else:
        print("\n[AVISO] Todavía no hay artistas registrados en el Overpalooza\nPor favor, intente nuevamente más adelante.\n")
        funciones.pedir_opcion_valida("\nIngresar (1) para volver al menú anterior: ", [1])
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

def consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados):
    """
    Recibe la matriz lineup, las tuplas de horarios y escenarios, las listas de artistas y códigos, y los acumuladores de venta.
    No retorna un valor; muestra la grilla de programacion del festival por código y por nombre de artista, y permite volver al menú principal.
    """
    print("\nMENÚ: Consultar grilla")
    print('\n1. Ver lineup\n2. Salir\n')

    opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2])

    if opcion == 1:
        print('\nLINEUP ACTUAL\n')

        print("\nLINEUP POR CÓDIGO\n")
        funciones.imprimir_grilla(lineup, horarios, escenarios)
        print('\n\n')

        print('=' * 63)

        print("\n\nLINEUP POR NOMBRE\n")

        funciones.imprimir_grilla_con_nombres(lineup, horarios, escenarios, codigos, nombre_artistas)


        funciones.pedir_opcion_valida("\nIngresar (1) para volver al menú anterior: ", [1])
        consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

    elif opcion == 2:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

def registrar_artistas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados, registrados=0):
    """
    Recibe las mismas estructuras que modificar_programacion, mas un contador de artistas
    registrados en esta tanda (arranca en 0).
    No retorna un valor.
    """
    if registrados >= 30:
        print("[AVISO] No se pueden ingresar más artistas: ya se alcanzó el límite de 30 artistas registrados.")
        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
    else:
        funciones.ingresar_artista(lineup, nombre_artistas, codigos)
        print("\nPara continuar ingresando artistas, presione (1). Para detener el registro, presione (2).")
        volver = funciones.pedir_opcion_valida('Ingresar:', [1, 2])

        if volver == 2:
            modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
        else:
            registrar_artistas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados, registrados + 1)

def elegir_artista_a_modificar(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados, modificar_artista=None):
    """
    Recibe las mismas estructuras que modificar_programacion, mas el código ya tipeado (o None
    la primera vez, en cuyo caso se pide por teclado).
    Retorna el código válido y ya registrado que ingresó el usuario, o None si el usuario
    decidió salir (ingresando '2').
    """
    if modificar_artista is None:
        modificar_artista = input("Ingresar codigo del artista a modificar, o (2) para salir: ").upper()

    if modificar_artista == '2':
        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
        return None
    elif funciones.validar_codigo(modificar_artista) and modificar_artista in codigos:
        return modificar_artista
    else:
        if not funciones.validar_codigo(modificar_artista):
            print("[ERROR] Código inválido. Por favor, ingrese un código con el formato 'A-XX'.")
        else:
            print('[ERROR] El código ingresado no se encuentra registrado. Por favor, ingrese un código válido.\n')
        nuevo_codigo = input("Ingresar codigo del artista a modificar: ").upper()
        return elegir_artista_a_modificar(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados, nuevo_codigo)

def modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados):
    """
    Recibe la matriz lineup, las listas de artistas y codigos, los acumuladores de venta y las tuplas de horarios y escenarios.
    No retorna un valor; permite registrar nuevos artistas o modificar los datos de un artista ya registrado (código, nombre, horario o escenario), y permite volver al menú principal.
    """
    print("\nMENÚ: Modificar programación")
    print('\n1. Registrar artista\n2. Modificar artista\n3. Salir\n')

    opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2, 3])

    if opcion == 1:
        print("MENÚ: Registrar artista")
        registrar_artistas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
    elif opcion == 2:
        print("MENU: Modificar artista\n")
        if not codigos:
            print("[AVISO] Todavía no se ha registrado ningún artista.\n")
            funciones.pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])
            modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
        else:
            for i in range(len(codigos)):
                print(f'Artista {i+1}: {codigos[i]} - {nombre_artistas[i]}\n')

            modificar_artista = elegir_artista_a_modificar(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)

            if modificar_artista is not None:
                indice = codigos.index(modificar_artista)
                print('Ingresar el número del dato a modificar:\n1. Modificar código del artista\n2. Cambiar nombre del artista\n3. Cambiar horario\n4. Cambiar escenario')

                modificar_datos = funciones.pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4])
                if modificar_datos == 1:
                    codigo_nuevo = (input("Ingresar un código nuevo: ")).upper()
                    while not funciones.validar_codigo(codigo_nuevo) or funciones.artista_ya_ingresado(codigo_nuevo, codigos):
                        if not funciones.validar_codigo(codigo_nuevo):
                            print("[ERROR] Código inválido. Por favor, ingrese un código con el formato 'A-XX'.")
                        else:
                            print(f"[ERROR] El código {codigo_nuevo} ya está en uso por otro artista.")
                        codigo_nuevo = input("Ingresar codigo nuevo: ").upper()
                    funciones.cambiar_artista(lineup, codigos, indice, codigo_nuevo)
                    print(f"El código del artista {nombre_artistas[indice]} fue actualizado a {codigo_nuevo}.")

                    volver = funciones.pedir_opcion_valida("ingresar (1) para volver al menú anterior: ", [1])
                    if volver == 1:
                        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)

                elif modificar_datos == 2:
                    nombre = input("Ingresar el nombre nuevo: ")
                    nombre_artistas[indice] = nombre
                    print(f"El nombre del artista {codigos[indice]} fue actualizado a {nombre}.")
                    volver = funciones.pedir_opcion_valida("ingresar (1) para volver al menú anterior: ", [1])
                    if volver == 1:
                        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
                elif modificar_datos == 3:
                    horario_viejo, escenario_viejo = funciones.buscar_posicion_en_lineup(lineup, modificar_artista)
                    verificacion = funciones.chequear_artista(lineup, modificar_artista)
                    if verificacion:
                        horario_nuevo = funciones.pedir_opcion_valida("Ingresar el nuevo horario: ", [1, 2, 3, 4, 5, 6, 7, 8])
                        horario_nuevo = funciones.validar_horario(horario_nuevo, lineup, escenario_viejo)

                        lineup[horario_viejo-1][escenario_viejo-1] = '.'
                        lineup[horario_nuevo-1][escenario_viejo-1] = modificar_artista
                        print(f"El artista {modificar_artista} fue reasignado al horario {horario_nuevo}.")
                    volver = funciones.pedir_opcion_valida("ingresar (1) para volver al menú anterior: ", [1])
                    if volver == 1:
                        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
                elif modificar_datos == 4:
                    horario_viejo, escenario_viejo = funciones.buscar_posicion_en_lineup(lineup, modificar_artista)

                    escenario_nuevo = funciones.pedir_opcion_valida("Ingresar el nuevo escenario: ", [1, 2, 3, 4, 5])
                    escenario_nuevo = funciones.validar_escenario(escenario_nuevo, lineup, horario_viejo)

                    lineup[horario_viejo-1][escenario_viejo-1] = '.'
                    lineup[horario_viejo-1][escenario_nuevo-1] = modificar_artista
                    print(f"El artista {modificar_artista} fue reasignado al escenario {escenario_nuevo}.")

                    volver = funciones.pedir_opcion_valida("ingresar (1) para volver al menú anterior: ", [1])
                    if volver == 1:
                        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)

    elif opcion == 3:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

def menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos, general, vip, escenarios_rankeados, escenarios):
    """
    Recibe los acumuladores de venta, la configuracion de entradas, la capacidad general,
    el maximo por operacion y las estructuras de programacion del festival.
    No retorna un valor; gestiona la compra de entradas General y VIP y muestra la disponibilidad restante, permitiendo volver al menú principal.
    """
    print("\nMENU: Comprar entradas")
    disponibilidad = funciones.calcular_disponibilidad_general(vendidas_gen + vendidas_vip, capacidad_general)
    disponibilidad_gen = funciones.calcular_disponibilidad_general(vendidas_gen, general[1])
    disponibilidad_vip = funciones.calcular_disponibilidad_general(vendidas_vip, vip[1])

    if disponibilidad == 0:
        print("\nLas entradas están agotadas! Muchas gracias por apoyar OVERPALOOZA")
    if disponibilidad <= 20 and disponibilidad > 0:
        print("AVISO".center(20, "-"))
        print("Queda menos del 20% de las entradas. ¡Consigue la tuya rápido!")
    if disponibilidad_gen == 0 and disponibilidad_vip > 0:
        print("Las entradas generales se han agotado!")
    elif disponibilidad_vip == 0 and disponibilidad_gen > 0:
        print("AVISO".center(20, "-"))
        print("Las entradas VIP se han agotado!")

    print("\n1. Comprar entradas\n2. Chequear disponibilidad\n3. Salir\n")
    opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2, 3])

    if opcion == 1:
        if disponibilidad <= 0:
            print("\nLas entradas están agotadas! Muchas gracias por apoyar OVERPALOOZA")
        else:
            print(f'\nGeneral: ${entradas[0][0]} \nVIP: ${entradas[1][0]}')
            print("\nQue tipo de entradas queres comprar?")
            print("1. General\n2. VIP\n")
            tipo = funciones.pedir_opcion_valida("Ingresar: ", [1, 2])

            if tipo == 1:
                if disponibilidad_gen == 0:
                    print("\nLas entradas generales se han agotado!")
                else:
                    tot, venta_tot, vendidas_gen, vendidas_vip, exito = funciones.comprar_entradas(
                        tot, venta_tot, entradas, tipo, vendidas_gen, vendidas_vip, max_operacion)
                    if exito:
                        print("TU COMPRA HA SIDO EXITOSA!".center(40, '='))
                        funciones.encuesta_escenario(escenarios, escenarios_rankeados)
            elif tipo == 2:
                if disponibilidad_vip == 0:
                    print("\nLas entradas VIP se han agotado!")
                else:
                    tot, venta_tot, vendidas_gen, vendidas_vip, exito = funciones.comprar_entradas(
                        tot, venta_tot, entradas, tipo, vendidas_gen, vendidas_vip, max_operacion)
                    if exito:
                        print("TU COMPRA HA SIDO EXITOSA!".center(40, '='))
                        funciones.encuesta_escenario(escenarios, escenarios_rankeados)

        funciones.pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: \n", [1])
        menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos, general, vip, escenarios_rankeados, escenarios)

    elif opcion == 2:
        print(f'\nTodavía queda el {disponibilidad:.2f}% de las entradas\n')
        funciones.pedir_opcion_valida("\nIngresar (3) para volver al menu anterior: \n", [3])
        menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos, general, vip, escenarios_rankeados, escenarios)

    elif opcion == 3:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

def estadisticas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, capacidad_general, entradas, escenarios_rankeados):
    """
    Recibe las estructuras de programacion del festival, los acumuladores de venta, la capacidad general y la configuracion de entradas.
    No retorna un valor; muestra los distintos informes y estadisticas del sistema segun la opcion elegida.
    """
    print("\n1. Ranking mejores escenarios por votación\n2. Información de entradas\n3. Recaudación total\n4. Porcentaje de ocupación\n5. Salir\n")

    opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4, 5])

    if opcion == 5:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    else:
        if opcion == 1:
            print("Los mejores escenarios elegidos por votación son:")
            funciones.mostrar_ranking(escenarios, escenarios_rankeados)
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

        volver = funciones.pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])
        if volver == 1:
            estadisticas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, capacidad_general, entradas, escenarios_rankeados)



