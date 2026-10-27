from funciones import *

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
    while True:
        print("✦   ★   ✦   ★   ✦   ★   ✦   ★")
        print("   B I E N V E N I D O   A L")
        print("     O V E R P A L O O Z A")
        print("✦   ★   ✦   ★   ✦   ★   ✦   ★")
        print()

        print("Ingresar tipo de cuenta para iniciar sesion:")

        print("\n1. Iniciar sesión\n2. Crear Cuenta\n3. Salir\n")

        tipo_ingreso = pedir_opcion_valida("Ingresar:", [1, 2, 3])

        if tipo_ingreso == 1:
            nombre = validacion_nombre()
            contrasena = input("Ingresar contraseña: ")

            rol = buscar_usuarios(nombre, contrasena)
            if rol == 'Admin':
                print("\nCuenta de Admin encontrada! Login exitoso\n")
                menu_admin(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados, horarios, escenarios, capacidad_general, entradas)

            elif rol == "Usuario": 
                print("\nCuenta de Usuario encontrada! Login exitoso\n")
                menu_usuario(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados, horarios, escenarios, capacidad_general, entradas, max_operacion, general, vip)

            else:
                print("ERROR, CUENTA NO ENCONTRADA.")

        elif tipo_ingreso == 2:
            print("Bienvenido a la creación de cuentas!")

            nombre = validacion_nombre()
            contrasena = validacion_contrasena()
            mail = validacion_mail()

            if repitencia_usuarios(nombre, mail):
                print("El usuario ya esta registrado. Ingresar otro.")
            else:
                registrar_cuenta(nombre, contrasena, mail)
        if tipo_ingreso == 3:
            print("="*60)
            print('¡Gracias por asistir al OVERPALOOZA!'.center(60, '-'))
            print("="*60)
            break

def menu_admin(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados, horarios, escenarios, capacidad_general, entradas):
    while True:
        print("\nMENU ADMIN\n")

        print("1. Consultar grilla\n2. Modificar programación\n3. Estadísticas\n4. Salir")

        opcion = pedir_opcion_valida("Elegir opción (4 para finalizar): ", [1, 2, 3, 4])

        if opcion == 1:
            consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos)
        elif opcion == 2:
            modificar_programacion(lineup, nombre_artistas, codigos, horarios, escenarios)
        elif opcion == 3:
            estadisticas(lineup, venta_tot, vendidas_gen, vendidas_vip, escenarios, capacidad_general, entradas, escenarios_rankeados)
        elif opcion == 4:
            print("="*60)
            print('¡Gracias por asistir al OVERPALOOZA!'.center(60, '-'))
            print("="*60)
            break

def menu_usuario(lineup, nombre_artistas, codigos, tot, venta_tot, vendidas_gen, vendidas_vip, escenarios_rankeados, horarios, escenarios, capacidad_general, entradas, max_operacion, general, vip):
    while True:
        print("\nMENU Usuario\n")

        print("1. Consultar información\n2. Buscar artista\n3. Consultar grilla\n4. Comprar entradas\n5. Estadisticas\n6. Salir")

        opcion = pedir_opcion_valida("Elegir opción (6 para finalizar): ", [1, 2, 3, 4, 5, 6])
        if opcion == 1:
            consultar_informacion()
        elif opcion == 2:
            menu_buscar_artista(lineup, nombre_artistas, codigos, escenarios, horarios)
        elif opcion == 3:
            consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos)
        elif opcion == 4:
            # Recibe y pisa los valores viejos!!
            tot, venta_tot, vendidas_gen, vendidas_vip = menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, general, vip, escenarios_rankeados, escenarios)
        elif opcion == 5:
            estadisticas(lineup, venta_tot, vendidas_gen, vendidas_vip, escenarios, capacidad_general, entradas, escenarios_rankeados)
        elif opcion == 6:
            print("="*60)
            print('¡Gracias por asistir al OVERPALOOZA!'.center(60, '-'))
            print("="*60)
            break

def consultar_informacion():
    """
    Recibe la matriz lineup, las listas de artistas y codigos, y los acumuladores de venta.
    No retorna un valor, muestra el submenú de información general del festival y la informacion correspondiente a la opción elegida por el usuario.
    """
    while True:
        print("✦" + "═" * 44 + "✦")
        print(f"✦{' MENÚ: Consultar información '.center(44, '═')}✦ ")
        print("│ 1. SPONSORS \n│ 2. INGRESO Y APERTURA \n│ 3. OBJETOS NO PERMITIDOS \n│ 4. REDES SOCIALES \n│ 5. Salir")
        print("✦" + "═" * 44 + "✦")

        opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4, 5])
        if opcion == 1:
            print("SPONSORS".center(35, "="))
            print(f"│ {'PRESENTA':<15}: Personal y FLOW")
            print(f"│ {'MEDIOS DE PAGO':<15}: VISA y Santander")
            print(f"│ {'INVITA':<15}: Fiat")
            print(f"│ {'AUSPICIA':<15}: McDonalds")
            print(f"│ {'PRODUCE':<15}: DfEntertainment\n")
            opcion = pedir_opcion_valida("Ingrese (1) para volver al menú anterior: ", [1])
        elif opcion == 2:
            print("INGRESO Y APERTURA".center(35, "="))
            print("│ Las puertas del OVERPALOOZA se abrirán a las 11:00AM para el ingreso del público. \n│ ¡Te esperamos!\n")
            opcion = pedir_opcion_valida("Ingrese (1) para volver al menú anterior: ", [1])
        elif opcion == 3:
            print("OBJETOS NO PERMITIDOS".center(35, "="))
            print("\n│🛇  Elementos punzantes \n│🛇  Paraguas \n│🛇  Computadoras \n│🛇  Alcohol \n│🛇  Carteles políticos o religiosos \n│🛇  Alimentos o bebidas \n│🛇  Encendedores \n│🛇  Bengalas \n│🛇  Drones \n")
            opcion = pedir_opcion_valida("Ingrese (1) para volver al menú anterior: ", [1])
        elif opcion == 4:
            print("REDES SOCIALES".center(35, "="))
            print(f"│ {'INSTAGRAM':<15}: overpaloozaar")
            print(f"│ {'FACEBOOK':<15}: overpalooza.ar")
            print(f"│ {'YOUTUBE':<15}: OverpaloozaARG")
            print(f"│ {'TWITTER (X)':<15}: Overpaloozaar \n")
            opcion = pedir_opcion_valida("Ingrese (1) para volver al menú anterior: ", [1])
        elif opcion == 5:
            break

def menu_buscar_artista(lineup, nombre_artistas, codigos, escenarios, horarios):
    """
    Recibe la matriz lineup, las listas de artistas y codigos, los acumuladores de venta y las tuplas de escenarios y horarios.
    No retorna un valor; permite buscar un artista por código o nombre, mostrando su información correspondiente, y permite volver al menú principal.
    """
    while True:                                   
        print("✦" + "═" * 44 + "✦")
        print(f"✦{' MENÚ: Buscar artista '.center(44, '═')}✦")
        print("✦" + "═" * 44 + "✦")
        if codigos:
            print("│ 1. Ingresar artista a buscar \n│ 2. Salir\n")
            print("✦" + "═" * 44 + "✦")
            opcion = pedir_opcion_valida("Ingresar: ", [1, 2])
            if opcion == 1:
                imprimir_artistas_ordenados(nombre_artistas)
                buscado = (input("\nIngresar código o nombre del artista a buscar, o (2) para salir: ")).strip().lower()

                if buscado == "2":
                    break
                else:
                    while buscado not in [n.lower() for n in nombre_artistas] and buscado not in [c.lower() for c in codigos] and buscado != "2":
                        print("[ERROR] Ingrese un código o nombre válido.")
                        opcion_a = pedir_opcion_valida("(1) Para intentarlo nuevamente, (2) para salir: ", [1, 2])

                        if opcion_a == 1:
                            buscado = (input("\nIngresar código o nombre del artista a buscar: ")).strip().lower()
                        else:
                            buscado = "2"

                    if buscado == "2":
                        break
                    else:
                        nombre, escenario, horario = buscar_artista(buscado, codigos, nombre_artistas, lineup, escenarios, horarios)
                        print(f"\nArtista: {nombre}")
                        print(f"Escenario: {escenario}")
                        print(f"Horario: {horario}")

                        pedir_opcion_valida("\nIngresar (1) para volver al menú anterior: ", [1])

            else:
                break
        else:
            print("\n[AVISO] Todavía no hay artistas registrados en el Overpalooza.\nPor favor, intente nuevamente más adelante.\n")
            pedir_opcion_valida("\nIngresar (1) para volver al menú anterior: ", [1])
            break

def consultar_grilla(lineup, horarios, escenarios, nombre_artistas, codigos):
    """
    Recibe la matriz lineup, las tuplas de horarios y escenarios, las listas de artistas y códigos, y los acumuladores de venta.
    No retorna un valor; muestra la grilla de programacion del festival por código y por nombre de artista, y permite volver al menú principal.
    """
    while True:
        print("✦" + "═" * 44 + "✦")
        print(f"✦{' MENÚ: Consultar grilla '.center(44, '═')}✦")
        print("✦" + "═" * 44 + "✦")
        print('\n1. Ver lineup\n2. Salir')
        print("✦" + "═" * 44 + "✦")

        opcion = pedir_opcion_valida("Ingresar: ", [1, 2])

        if opcion == 1:
            print("✦" + "═" * 44 + "✦")
            print(f"✦{' LINEUP ACTUAL '.center(44, '═')}✦")
            print("✦" + "═" * 44 + "✦")

            print("\nLINEUP POR CÓDIGO\n")
            imprimir_grilla(lineup, horarios, escenarios)
            print('\n')

            print("\n\nLINEUP POR NOMBRE\n")

            imprimir_grilla_con_nombres(lineup, horarios, escenarios, codigos, nombre_artistas)

            pedir_opcion_valida("\nIngresar (1) para volver al menú anterior: ", [1])

        elif opcion == 2:
            break

def registrar_artistas(lineup, nombre_artistas, codigos, horarios, escenarios):
    """
    Recibe las mismas estructuras que modificar_programacion. 
    No retorna un valor; permite la carga consecutiva de artistas controlando no superar el límite
    máximo de 30, y vuelve al menú de programación al finalizar la carga.
    """
    while True:
        if len(codigos) >= 30:
            print("[AVISO] No se pueden ingresar más artistas: ya se alcanzó el límite de 30 artistas registrados.")
            break

        ingresar_artista(lineup, nombre_artistas, codigos, horarios, escenarios)
        print("\nPara continuar ingresando artistas, presione (1). Para detener el registro, presione (2).")
        volver = pedir_opcion_valida('Ingresar:', [1, 2])

        if volver == 2:
            break

def elegir_artista_a_modificar(codigos, modificar_artista=None):
    """
    Recibe las mismas estructuras que modificar_programacion, mas el código ya tipeado (o None
    la primera vez, en cuyo caso se pide por teclado).
    Retorna el código válido y ya registrado que ingresó el usuario, o None si el usuario
    decidió salir (ingresando '2').
    """
    while True:
        if modificar_artista is None:
            modificar_artista = input("Ingresar código del artista a modificar, o (2) para salir: ").upper()
            
        if modificar_artista == '2':
            return None
        elif validar_codigo(modificar_artista) and modificar_artista in codigos:
            return modificar_artista
        else:
            if not validar_codigo(modificar_artista):
                print("[ERROR] Código inválido. Por favor, ingrese un código con el formato 'A-XX'.")
            else:
                print('[ERROR] El código ingresado no se encuentra registrado. Por favor, ingrese un código válido.\n')
            modificar_artista = input("Ingresar código del artista a modificar: ").upper()
        
def modificar_programacion(lineup, nombre_artistas, codigos, horarios, escenarios):
    """
    Recibe la matriz lineup, las listas de artistas y codigos, los acumuladores de venta y las tuplas de horarios y escenarios.
    No retorna un valor; permite registrar nuevos artistas o modificar los datos de un artista ya registrado (código, nombre, horario o escenario), y permite volver al menú principal.
    """
    while True:
        print("✦" + "═" * 44 + "✦")
        print(f"✦{' MENÚ: Modificar programación '.center(44, '═')}✦")
        print("✦" + "═" * 44 + "✦")
        print("│ 1. Registrar artista\n│ 2. Modificar artista\n│ 3. Salir")
        print("✦" + "═" * 44 + "✦")

        opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3])

        if opcion == 1:
            print("✦" + "═" * 44 + "✦")
            print(f"✦{' MENÚ: Registrar artista '.center(44, '═')}✦")
            print("✦" + "═" * 44 + "✦")
            registrar_artistas(lineup, nombre_artistas, codigos, horarios, escenarios)
        elif opcion == 2:
            print("✦" + "═" * 44 + "✦")
            print(f"✦{' MENÚ: Modificar artista '.center(44, '═')}✦")
            print("✦" + "═" * 44 + "✦")
            if not codigos:
                print("[AVISO] Todavía no se ha registrado ningún artista.\n")
                pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])
            else:
                for i in range(len(codigos)):
                    print(f'Artista {i+1}: {codigos[i]} - {nombre_artistas[i]}\n')

                modificar_artista = elegir_artista_a_modificar(codigos)

                if modificar_artista is not None:
                    indice = codigos.index(modificar_artista)
                    print('Ingresar el número del dato a modificar:\n1. Modificar código del artista\n2. Cambiar nombre del artista\n3. Cambiar horario\n4. Cambiar escenario')

                    modificar_datos = pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4])
                    if modificar_datos == 1:
                        codigo_nuevo = (input("Ingresar un código nuevo: ")).upper()
                        while not validar_codigo(codigo_nuevo) or artista_ya_ingresado(codigo_nuevo, codigos):
                            if not validar_codigo(codigo_nuevo):
                                print("[ERROR] Código inválido. Por favor, ingrese un código con el formato 'A-XX'.")
                            else:
                                print(f"[ERROR] El código {codigo_nuevo} ya está en uso por otro artista.")
                            codigo_nuevo = input("Ingresar codigo nuevo: ").upper()
                        cambiar_artista(lineup, codigos, indice, codigo_nuevo)
                        print(f"El código del artista {nombre_artistas[indice]} fue actualizado a {codigo_nuevo}.")

                        volver = pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])

                    elif modificar_datos == 2:
                        nombre = input("Ingresar el nombre nuevo: ")
                        while nombre == "" or nombre.isspace():
                            print("[ERROR] El nombre no puede quedar vacío ni contener únicamente espacios en blanco.")
                            nombre = input("Ingresar el nombre nuevo: ")
                        nombre_artistas[indice] = nombre
                        print(f"El nombre del artista {codigos[indice]} fue actualizado a {nombre}.")
                        volver = pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])

                    elif modificar_datos == 3:
                        horario_viejo, escenario_viejo = buscar_posicion_en_lineup(lineup, modificar_artista)
                        verificacion = chequear_artista(lineup, modificar_artista)
                        if verificacion:
                            horario_nuevo = pedir_opcion_valida("Ingresar el nuevo horario: ", [1, 2, 3, 4, 5, 6, 7, 8])
                            horario_nuevo = validar_horario(horario_nuevo, lineup, escenario_viejo)

                            lineup[horario_viejo-1][escenario_viejo-1] = '.'
                            lineup[horario_nuevo-1][escenario_viejo-1] = modificar_artista
                            print(f"El artista {modificar_artista} fue reasignado al horario {horario_nuevo}.")
                        volver = pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])

                    elif modificar_datos == 4:
                        horario_viejo, escenario_viejo = buscar_posicion_en_lineup(lineup, modificar_artista)

                        escenario_nuevo = pedir_opcion_valida("Ingresar el nuevo escenario: ", [1, 2, 3, 4, 5])
                        escenario_nuevo = validar_escenario(escenario_nuevo, lineup, horario_viejo)

                        lineup[horario_viejo-1][escenario_viejo-1] = '.'
                        lineup[horario_viejo-1][escenario_nuevo-1] = modificar_artista
                        print(f"El artista {modificar_artista} fue reasignado al escenario {escenario_nuevo}.")
                        volver = pedir_opcion_valida("Ingresar (1) para volver al menú anterior: ", [1])

        elif opcion == 3:
            break
        
def pedir_cantidad_entradas(limite):
    """
    Pide por teclado la cantidad de entradas a comprar, validando formato y límite.
    Retorna la cantidad válida ingresada.
    """
    print("\nIngrese la cantidad de entradas que desea comprar.")
    entrada_usuario = input("Ingresar: ")
    while not es_cantidad_valida(entrada_usuario):
        print("[ERROR] No fue posible realizar la compra. La cantidad ingresada no es un número válido.")
        entrada_usuario = input("Ingresar: ")

    cantidad = int(entrada_usuario)
    while cantidad > limite:
        print(f"[ERROR] Puede comprar como máximo {limite} entradas en esta operación.")
        entrada_usuario = input("Ingresar:")
        while not es_cantidad_valida(entrada_usuario):
            print("[ERROR] No fue posible realizar la compra. La cantidad ingresada no es un número válido.")
            entrada_usuario = input("Ingresar: ")
        cantidad = int(entrada_usuario)

    return cantidad

def menu_comprar_entradas(tot, venta_tot, entradas, vendidas_gen, vendidas_vip, capacidad_general, max_operacion, general, vip, escenarios_rankeados, escenarios):
    """
    Recibe los acumuladores de venta, las configuraciones de entradas, la capacidad total, el límite de compra por operación y las estructuras de artistas y escenarios.
    No retorna un valor; gestiona la compra de entradas General y VIP, chequea la disponibilidad 
    restante y llama a la encuesta de escenarios tras una operación exitosa.
    """
    while True:
        print("✦" + "═" * 44 + "✦")
        print(f"✦{' MENÚ: Comprar entradas '.center(44, '═')}✦")
        print("✦" + "═" * 44 + "✦")
        disponibilidad = calcular_disponibilidad_general(vendidas_gen + vendidas_vip, capacidad_general)
        disponibilidad_gen = calcular_disponibilidad_general(vendidas_gen, general[1])
        disponibilidad_vip = calcular_disponibilidad_general(vendidas_vip, vip[1])

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
        opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3])

        if opcion == 1:
            print("=" * 50)
            print("◆ PRECIOS ◆".center(50, "-"))
            print(f'│ General: ${entradas[0][0]} \n│ VIP: ${entradas[1][0]}')
            print("\n¿Qué tipo de entradas querés comprar?")
            print("1. General\n2. VIP\n")
            tipo = pedir_opcion_valida("Ingresar: ", [1, 2])

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
                limite = calcular_limite_compra(tipo, entradas, vendidas_gen, vendidas_vip, max_operacion)
                cantidad = pedir_cantidad_entradas(limite)

                confirmar = pedir_opcion_valida(f'\n[ATENCION] Estás por comprar {cantidad} entrada(s). Para confirmar su compra, ingrese (1). De lo contrario, ingrese (2) para salir: ',[1, 2])

                if confirmar == 1:
                    importe = calcular_importe_compra(tipo, entradas, cantidad)
                    tot += cantidad
                    venta_tot += importe
                    if tipo == 1:
                        vendidas_gen += cantidad
                    else:
                        vendidas_vip += cantidad
                    print("✦" + "═" * 44 + "✦")
                    print(f"✦{' ¡TU COMPRA HA SIDO EXITOSA! '.center(44, '═')}✦")
                    print("✦" + "═" * 44 + "✦")

            pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])
        
        elif opcion == 2:
            print("=" * 50)
            print("DISPONIBILIDAD".center(50, "-"))
            print("=" * 50)
            print(f'\nTodavía queda el {disponibilidad:.2f}% de las entradas.')
            pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])

        elif opcion == 3:
            break
    return tot, venta_tot, vendidas_gen, vendidas_vip

def estadisticas(lineup, venta_tot, vendidas_gen, vendidas_vip, escenarios, capacidad_general, entradas, escenarios_rankeados):
    """
    Recibe las estructuras de programacion del festival, los acumuladores de venta, la capacidad general y la configuracion de entradas.
    No retorna un valor; muestra los distintos informes y estadisticas del sistema segun la opcion elegida.
    """
    while True:
        print("✦" + "═" * 44 + "✦")
        print(f"✦{' MENÚ: Estadísticas e informes '.center(44, '═')}✦")
        print("✦" + "═" * 44 + "✦")
        print("│ 1. Entradas generales\n│ 2. Entradas VIP\n│ 3. Recaudación total\n│ 4. Porcentaje de ocupación\n│ 5. Total de artistas asignados\n│ 6. Celdas asignadas / libres\n│ 7. Ingresos fallidos de ingreso\n│ 8. Salir")
        print("✦" + "═" * 44 + "✦")

        opcion = pedir_opcion_valida("Ingresar: ", [1, 2, 3, 4, 5, 6])

        if opcion == 6:
            break
        else:
            if opcion == 1:
                print("=" * 50)
                print("ENTRADAS GENERALES".center(50, "-"))
                print("=" * 50, "\n")

                pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])
            elif opcion == 2:
                print("=" * 50)
                print("ENTRADAS VIP".center(50, "-"))
                print("=" * 50, "\n")

                pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])
            elif opcion == 3:
                print("=" * 50)
                print("RECAUDACIÓN TOTAL ACUMULADA".center(50, "-"))
                print("=" * 50, "\n")
                print(f"La recaudación total es de: ${venta_tot}")
                pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])
            elif opcion == 4:
                print("=" * 50)
                print("PORCENTAJE DE OCUPACIÓN".center(50, "-"))
                print("=" * 50, "\n")
                porcentaje = 100 - calcular_disponibilidad_general(vendidas_gen + vendidas_vip, capacidad_general)
                print(f"Porcentaje de ocupación: {porcentaje:.2f}%")
                pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])
            elif opcion == 5:
                print("=" * 50)
                print("TOTAL DE ARTISTAS ASIGNADOS EN EL SISTEMA".center(50, "-"))
                print("=" * 50, "\n")
            
            elif opcion == 6:
                print("=" * 50)
                print("ESCENARIOS ASIGNADOS / ESCENARIOS LIBRES".center(50, "-"))
                print("=" * 50, "\n")
                
            elif opcion == 7:
                print("=" * 50)
                print("INTENTOS FALLIDOS DE INGRESO".center(50, "-"))
                print("=" * 50, "\n")
                
                pedir_opcion_valida("\nIngresar (1) para volver al menu anterior: ", [1])



