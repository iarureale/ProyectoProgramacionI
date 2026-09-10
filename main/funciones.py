def grilla():
    """
    Establecemos las filas (horarios) y columnas (escenarios) con su respectivo valor para
    crear la matriz (lineup) mediante una lista por comprensión.
    Retorna lineup
    """
    escenarios = 5
    horarios = 8
    lineup = [['.' for c in range(escenarios)] for f in range(horarios)]

    return lineup

def artista_ya_ingresado(codigo, codigos):
    """
    Recorre toda la matriz en busca del artista. Retorna true si lo encuentra.
    No se encuentra "while artista in lineup" debido a que chequearia si toda la fila equivale a artista
    """
    if codigo in codigos:
        return True
    return False


def ingresar_artista(lineup, nombre_artistas, codigos):
    if len(codigos) >= 30:
        print("No se pueden ingresar más artistas, ya se alcanzó el límite de 30")
        return
    
    codigo = input("Ingresar codigo del artista a insertar: ").upper()
    while not validar_codigo(codigo):
        print("ERROR. Ingresé un código válido. ('A-XX')")
        codigo = input("Ingresar codigo del artista a insertar: ").upper()

    while artista_ya_ingresado(codigo, codigos):
        print(f'{codigo} ya esta ingresado en el lineup, Ingresar uno no ingresado')
        codigo = input("Ingresar artista a insertar: ").upper()

    codigos.append(codigo)
    nombre_artistico = input("Ingresar nombre del artista ingresado: ")

    nombre_artistas.append(nombre_artistico)

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

    print(f'Artista con código {codigo} asignado al horario {horario} y escenario {escenario} exitosamente.')

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
            valor = lineup[f][c] if lineup[f][c] != '.' else '.'
            print(f"{valor:<{ancho}}|", end="")
        print()

def comprar_entradas(tot, venta_tot, entradas, tipo, vendidas_gen, vendidas_vip, max_operacion, compras_tipo, compras_cantidad, compras_importe):
    """
    Registra una compra de entradas de tipo: General y VIP.
    Validad cantidad maxima por operacion y disponibilidad de las mismas antes de confirmar.
    Devuelve los acumuladores actualizados y ademas se agrega la operacion al registro de compras
    """
    print("\nIngresar entradas a comprar:\n")

    entradas_a_comprar = int(input())
    while entradas_a_comprar > max_operacion:
        print('\nLa cantidad ingresada supera la permitida por compra. Se permiten 6 por usuario\n')
        entradas_a_comprar = int(input('Ingresar entradas a comprar: '))

    importe = entradas_a_comprar * entradas[tipo - 1][0]
    tot += entradas_a_comprar
    venta_tot += importe

    if tipo == 1:
        vendidas_gen += entradas_a_comprar
    else:
        vendidas_vip += entradas_a_comprar

    compras_tipo.append("General" if tipo == 1 else "VIP")
    compras_cantidad.append(entradas_a_comprar)
    compras_importe.append(importe)

    return tot, venta_tot, vendidas_gen, vendidas_vip

def buscar_artista(buscado, codigos, nombre_artistas, lineup, escenario, horario):
    """
    Busca un artista por código o por nombre en las listas paralelas y luego en la grilla.
    Utilizando variables bandera como condición en los ciclos while para cortar la búsqueda. 
    Si no encuentra al artista, retorna (".")
    """
    buscado_limpio = buscado.strip().lower()
    indice_encontrado = []
    encontrado = False

    i = 0
    while i < len(codigos) and not encontrado:
        if codigos[i].lower() == buscado_limpio or nombre_artistas[i].lower() == buscado_limpio:
            indice_encontrado = i
            encontrado = True 
        i += 1

    if indice_encontrado == -1:
        print(f"No se encontró ningún artista con ese código o nombre. Vuelva a intentarlo.")
        return

    codigo_oficial = codigos[indice_encontrado]
    nombre_oficial = nombre_artistas[indice_encontrado]

    asignado = False
    escenario_asignado = "."
    horario_asignado = "."

    f = 0
    while f < len(lineup) and not asignado:
        c = 0
        while c < len(lineup[f]) and not asignado:
            if lineup[f][c] == codigo_oficial:
                escenario_asignado = escenario[c]
                horario_asignado = horario[f]
                asignado = True
            c += 1
        f += 1

    return nombre_oficial, escenario_asignado, horario_asignado


def comprar_entradas(tot, venta_tot, entradas, tipo, vendidas_gen, vendidas_vip, max_operacion):
    """
    Se piden cantidad de entradas a comprar (int) y valida que no supere el máximo a comprar por operación.
    El precio de entrada se define dependiendo el tipo de entrada a comprar (1 - GENERAL) (2 - VIP).
    Se acumula y retorna al total de entradas vendidas (tot), al total de recuadación (venta_tot) y al tipo de entrada
    adquirida (vendidas_gen o vendidas_vip) 
    """
    print("\nIngresar entradas a comprar:\n")

    entradas_a_comprar = int(input())
    while entradas_a_comprar > max_operacion:
        print('\nLa cantidad ingresada supera la permitida por compra. Se permiten 6 por usuario\n')
        entradas_a_comprar = int(input('Ingresar entradas a comprar: '))

    precio = entradas[tipo - 1][0] # tipo 1 -> general, tipo 2 -> vip
    tot += entradas_a_comprar
    venta_tot += entradas_a_comprar * precio
    # Contadores de entradas vendidas por tipo
    if tipo == 1:
        vendidas_gen += entradas_a_comprar
    else:
        vendidas_vip += entradas_a_comprar
    return tot, venta_tot, vendidas_gen, vendidas_vip


def calcular_disponibilidad_general(tot, capacidad):
    porcentaje = lambda tot, capacidad: (tot/capacidad) *100
    porcentaje_vendido = porcentaje(tot, capacidad)
    capacidad_general = 100 - porcentaje_vendido
    return capacidad_general

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
