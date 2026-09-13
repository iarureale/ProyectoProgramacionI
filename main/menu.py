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

    print("✦   ★   ✦   ★   ✦   ★   ✦   ★")
    print("   B I E N V E N I D O   A L")
    print("     O V E R P A L O O Z A")
    print("✦   ★   ✦   ★   ✦   ★   ✦   ★")
    print()
    print(" ✦ MENÚ PRINCIPAL ✦")
    print("=" * 20)
    print('1. Consultar información del festival \n2. Buscar artista\n3. Consultar grilla \n4. Comprar entradas \n5. Modificar programación\n6. Estadísticas e informes\n7. Salir')
    print("=" * 20)

    opcion = funciones.pedir_opcion_valida("Elegir opción (7 para finalizar): ", [1, 2, 3, 4, 5, 6, 7])

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
        print('¡Gracias por asistir al OVERPALOOZA!'.center(60, '-'))
        print("="*60)

def consultar_informacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados):
    """
    Recibe la matriz lineup, las listas de artistas y codigos, y los acumuladores de venta.
    No retorna un valor, muestra el submenú de información general del festival y la informacion correspondiente a la opción elegida por el usuario.
    """
    print("✦" + "═" * 44 + "✦")
    print(f"✦{' MENÚ: Consultar información '.center(44, '═')}✦ ")
    print("│ 1. SPONSORS \n│ 2. INGRESO Y APERTURA \n│ 3. OBJETOS NO PERMITIDOS \n│ 4. REDES SOCIALES \n│ 5. Salir")
    print("✦" + "═" * 44 + "✦")

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
        print("│ Las puertas del OVERPALOOZA se abrirán a las 11:00AM para el ingreso del público. \n│ ¡Te esperamos!\n")
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
    print("✦" + "═" * 44 + "✦")
    print(f"✦{' MENÚ: Buscar artista '.center(44, '═')}✦")
    print("✦" + "═" * 44 + "✦")
    if codigos:
        print("│ 1. Ingresar artista a buscar \n│ 2. Salir\n")
        print("✦" + "═" * 44 + "✦")
        opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2])
        if opcion == 1:
            funciones.imprimir_artistas_ordenados(nombre_artistas)
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
                    print(f"\nArtista: {nombre}")
                    print(f"Escenario: {escenario}")
                    print(f"Horario: {horario}")

                    funciones.pedir_opcion_valida("\nIngresar (1) para volver al menú anterior: ", [1])
                    menu_buscar_artista(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios, horarios, escenarios_rankeados)

        else:
            menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    else:
        print("\n[AVISO] Todavía no hay artistas registrados en el Overpalooza.\nPor favor, intente nuevamente más adelante.\n")
        funciones.pedir_opcion_valida("\nIngresar (1) para volver al menú anterior: ", [1])
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

def consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados):
    """
    Recibe la matriz lineup, las tuplas de horarios y escenarios, las listas de artistas y códigos, y los acumuladores de venta.
    No retorna un valor; muestra la grilla de programacion del festival por código y por nombre de artista, y permite volver al menú principal.
    """
    print("✦" + "═" * 44 + "✦")
    print(f"✦{' MENÚ: Consultar grilla '.center(44, '═')}✦")
    print("✦" + "═" * 44 + "✦")
    print('\n1. Ver lineup\n2. Salir')
    print("✦" + "═" * 44 + "✦")

    opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2])

    if opcion == 1:
        print("✦" + "═" * 44 + "✦")
        print(f"✦{' LINEUP ACTUAL '.center(44, '═')}✦")
        print("✦" + "═" * 44 + "✦")

        print("\nLINEUP POR CÓDIGO\n")
        funciones.imprimir_grilla(lineup, horarios, escenarios)
        print('\n')

        print("\n\nLINEUP POR NOMBRE\n")

        funciones.imprimir_grilla_con_nombres(lineup, horarios, escenarios, codigos, nombre_artistas)


        funciones.pedir_opcion_valida("\nIngresar (1) para volver al menú anterior: ", [1])
        consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

    elif opcion == 2:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

def registrar_artistas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados, registrados=0):
    """
    Recibe las mismas estructuras que modificar_programacion. 
    No retorna un valor; permite la carga consecutiva de artistas controlando no superar el límite
    máximo de 30, y vuelve al menú de programación al finalizar la carga.
    """
    if registrados >= 30:
        print("[AVISO] No se pueden ingresar más artistas: ya se alcanzó el límite de 30 artistas registrados.")
        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
    else:
        funciones.ingresar_artista(lineup, nombre_artistas, codigos, horarios, escenarios)
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
        modificar_artista = input("Ingresar código del artista a modificar, o (2) para salir: ").upper()

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
        nuevo_codigo = input("Ingresar código del artista a modificar: ").upper()
        return elegir_artista_a_modificar(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados, nuevo_codigo)

def modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados):
    """
    Recibe la matriz lineup, las listas de artistas y codigos, los acumuladores de venta y las tuplas de horarios y escenarios.
    No retorna un valor; permite registrar nuevos artistas o modificar los datos de un artista ya registrado (código, nombre, horario o escenario), y permite volver al menú principal.
    """
    print("✦" + "═" * 44 + "✦")
    print(f"✦{' MENÚ: Modificar programación '.center(44, '═')}✦")
    print("✦" + "═" * 44 + "✦")
    print("│ 1. Registrar artista\n│ 2. Modificar artista\n│ 3. Salir")
    print("✦" + "═" * 44 + "✦")

    opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2, 3])

    if opcion == 1:
        print("✦" + "═" * 44 + "✦")
        print(f"✦{' MENÚ: Registrar artista '.center(44, '═')}✦")
        print("✦" + "═" * 44 + "✦")
        registrar_artistas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
    elif opcion == 2:
        print("✦" + "═" * 44 + "✦")
        print(f"✦{' MENÚ: Modificar artista '.center(44, '═')}✦")
        print("✦" + "═" * 44 + "✦")
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

                    volver = funciones.pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])
                    if volver == 1:
                        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)

                elif modificar_datos == 2:
                    nombre = input("Ingresar el nombre nuevo: ")
                    while nombre == "" or nombre.isspace():
                        print("[ERROR] El nombre no puede quedar vacío ni contener únicamente espacios en blanco.")
                        nombre = input("Ingresar el nombre nuevo: ")
                    nombre_artistas[indice] = nombre
                    print(f"El nombre del artista {codigos[indice]} fue actualizado a {nombre}.")
                    volver = funciones.pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])
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
                    volver = funciones.pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])
                    if volver == 1:
                        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)
                elif modificar_datos == 4:
                    horario_viejo, escenario_viejo = funciones.buscar_posicion_en_lineup(lineup, modificar_artista)

                    escenario_nuevo = funciones.pedir_opcion_valida("Ingresar el nuevo escenario: ", [1, 2, 3, 4, 5])
                    escenario_nuevo = funciones.validar_escenario(escenario_nuevo, lineup, horario_viejo)

                    lineup[horario_viejo-1][escenario_viejo-1] = '.'
                    lineup[horario_viejo-1][escenario_nuevo-1] = modificar_artista
                    print(f"El artista {modificar_artista} fue reasignado al escenario {escenario_nuevo}.")

                    volver = funciones.pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])
                    if volver == 1:
                        modificar_programacion(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, escenarios_rankeados)

    elif opcion == 3:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

def pedir_cantidad_entradas(limite):
    """
    Pide por teclado la cantidad de entradas a comprar, validando formato y límite.
    Retorna la cantidad válida ingresada.
    """
    print("\nIngrese la cantidad de entradas que desea comprar.")
    entrada_usuario = input("Ingresar: ")
    while not funciones.es_cantidad_valida(entrada_usuario):
        print("[ERROR] No fue posible realizar la compra. La cantidad ingresada no es un número válido.")
        entrada_usuario = input("Ingresar: ")

    cantidad = int(entrada_usuario)
    while cantidad > limite:
        print(f"[ERROR] Puede comprar como máximo {limite} entradas en esta operación.")
        entrada_usuario = input("Ingresar:")
        while not funciones.es_cantidad_valida(entrada_usuario):
            print("[ERROR] No fue posible realizar la compra. La cantidad ingresada no es un número válido.")
            entrada_usuario = input("Ingresar: ")
        cantidad = int(entrada_usuario)

    return cantidad

def menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos, general, vip, escenarios_rankeados, escenarios):
    """
    Recibe los acumuladores de venta, las configuraciones de entradas, la capacidad total, el límite de compra por operación y las estructuras de artistas y escenarios.
    No retorna un valor; gestiona la compra de entradas General y VIP, chequea la disponibilidad 
    restante y llama a la encuesta de escenarios tras una operación exitosa.
    """
    print("✦" + "═" * 44 + "✦")
    print(f"✦{' MENÚ: Comprar entradas '.center(44, '═')}✦")
    print("✦" + "═" * 44 + "✦")
    disponibilidad = funciones.calcular_disponibilidad_general(vendidas_gen + vendidas_vip, capacidad_general)
    disponibilidad_gen = funciones.calcular_disponibilidad_general(vendidas_gen, general[1])
    disponibilidad_vip = funciones.calcular_disponibilidad_general(vendidas_vip, vip[1])

    if disponibilidad <= 0:
        print("=" * 50)
        print("¡Las entradas están agotadas!".center(50,"-"))
        print("Muchas gracias por apoyar OVERPALOOZA".center(50,"-"))
        print("=" * 50)
    if disponibilidad <= 20 and disponibilidad > 0:
        print("=" * 50)
        print("AVISO".center(50, "-"))
        print("=" * 50)
        print("Quedan menos del 20% de las entradas".center(50,"-"))
        print("¡Consigue la tuya rápido!".center(50,"-"))
    if disponibilidad_gen <= 0 and disponibilidad_vip > 0:
        print("=" * 50)
        print("¡Las entradas generales se han agotado!".center(50,"-"))
        print("=" * 50)
    elif disponibilidad_vip <= 0 and disponibilidad_gen > 0:
        print("=" * 50)
        print("¡Las entradas VIP se han agotado!".center(50,"-"))
        print("=" * 50)

    print("\n1. Comprar entradas\n2. Chequear disponibilidad\n3. Salir\n")
    opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2, 3])

    if opcion == 1:
        print("=" * 50)
        print("◆ PRECIOS ◆".center(50, "-"))
        print(f'│ General: ${entradas[0][0]} \n│ VIP: ${entradas[1][0]}')
        print("\n¿Qué tipo de entradas querés comprar?")
        print("1. General\n2. VIP\n")
        tipo = funciones.pedir_opcion_valida("Ingresar: ", [1, 2])

        if tipo == 1:
            disponibilidad_tipo = disponibilidad_gen
            nombre_tipo = "generales"
        else:
            disponibilidad_tipo = disponibilidad_vip
            nombre_tipo = "vip"

        if disponibilidad_tipo <= 0:
            print(f"{'=' * 50}\n")
            print(f"¡Las entradas {nombre_tipo} se han agotado!".center(50,"-"))
            print(f"\n{'=' * 50}")

        else:
            limite = funciones.calcular_limite_compra(tipo, entradas, vendidas_gen, vendidas_vip, max_operacion)
            cantidad = pedir_cantidad_entradas(limite)

            confirmar = funciones.pedir_opcion_valida(f'\n[ATENCION] Estás por comprar {cantidad} entrada(s). Para confirmar su compra, ingrese (1). De lo contrario, ingrese (2) para salir: ',[1, 2])

            if confirmar == 1:
                importe = funciones.calcular_importe_compra(tipo, entradas, cantidad)
                tot += cantidad
                venta_tot += importe
                if tipo == 1:
                    vendidas_gen += cantidad
                else:
                    vendidas_vip += cantidad
                print("✦" + "═" * 44 + "✦")
                print(f"✦{' ¡TU COMPRA HA SIDO EXITOSA! '.center(44, '═')}✦")
                print("✦" + "═" * 44 + "✦")
                funciones.encuesta_escenario(escenarios, escenarios_rankeados)

        funciones.pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])
        menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos, general, vip, escenarios_rankeados, escenarios)

    elif opcion == 2:
        print("=" * 50)
        print("DISPONIBILIDAD".center(50, "-"))
        print("=" * 50)
        print(f'\nTodavía queda el {disponibilidad:.2f}% de las entradas.')
        funciones.pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])
        menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, lineup, nombre_artistas, codigos, general, vip, escenarios_rankeados, escenarios)

    elif opcion == 3:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)

def estadisticas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, capacidad_general, entradas, escenarios_rankeados):
    """
    Recibe las estructuras de programacion del festival, los acumuladores de venta, la capacidad general y la configuracion de entradas.
    No retorna un valor; muestra los distintos informes y estadisticas del sistema segun la opcion elegida.
    """
    print("✦" + "═" * 44 + "✦")
    print(f"✦{' MENÚ: Estadísticas e informes '.center(44, '═')}✦")
    print("✦" + "═" * 44 + "✦")
    print("│ 1. Ranking mejores escenarios por votación\n│ 2. Información de entradas\n│ 3. Recaudación total\n│ 4. Porcentaje de ocupación\n│ 5. Escenarios con más y menos artistas asignados\n│ 6. Salir")
    print("✦" + "═" * 44 + "✦")

    opcion = funciones.pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4, 5, 6])

    if opcion == 6:
        menu_principal(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados)
    else:
        if opcion == 1:
            print("=" * 50)
            print("RANKING DE MEJORES ESCENARIOS POR VOTACIÓN".center(50, "-"))
            print("=" * 50, "\n")
            print("Los mejores escenarios elegidos por votación son:")
            funciones.mostrar_ranking(escenarios, escenarios_rankeados)
        elif opcion == 2:
            print("=" * 50)
            print("INFORMACIÓN DE ENTRADAS".center(50, "-"))
            print("=" * 50, "\n")
            precio_general = entradas[0][0]
            precio_vip = entradas[1][0]
            rec_gen = vendidas_gen * precio_general
            rec_vip = vendidas_vip * precio_vip
            print(f"General vendidas: {vendidas_gen}\nRecaudación General: ${rec_gen}")
            print(f'VIP vendidas: {vendidas_vip}\nRecaudación VIP: ${rec_vip}\n')
        elif opcion == 3:
            print("=" * 50)
            print("RECAUDACIÓN TOTAL".center(50, "-"))
            print("=" * 50, "\n")
            print(f"La recaudación total es de: ${venta_tot}")
        elif opcion == 4:
            print("=" * 50)
            print("PORCENTAJE DE OCUPACIÓN".center(50, "-"))
            print("=" * 50, "\n")
            porcentaje = 100 - funciones.calcular_disponibilidad_general(vendidas_gen + vendidas_vip, capacidad_general)
            print(f"Porcentaje de ocupación: {porcentaje:.2f}%")
        elif opcion == 5:
            print("=" * 50)
            print("ESCENARIOS CON MÁS Y MENOS ARTISTAS ASIGNADOS".center(50, "-"))
            print("=" * 50, "\n")

            conteo = funciones.contar_artistas_escenario(lineup, escenarios)

            if sum(conteo) == 0:
                print("[ADVERTENCIA] Para poder calcular este informe, tiene que haber al menos un artista asignado al lineup.")
            else:
                valor_max, escenarios_max, valor_min, escenarios_min = funciones.escenario_extremo(escenarios, conteo)

                if valor_max == valor_min:
                    print(f"¡Qué coincidencia! Todos los escenarios cuentan con la misma cantidad de artistas asignados ({valor_max} artista(s) cada uno).")
                else:
                    print(f"Escenario/s con más artistas ({valor_max} artista(s)):")
                    for nombre in escenarios_max:
                        print(f"✦ {nombre}")

                    print(f"\nEscenario/s con menos artistas ({valor_min} artista(s)):")
                    for nombre in escenarios_min:
                        print(f"✦ {nombre}")

        volver = funciones.pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])
        if volver == 1:
            estadisticas(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, horarios, escenarios, capacidad_general, entradas, escenarios_rankeados)



