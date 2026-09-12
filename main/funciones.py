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

def validar_escenario(escenario, lineup, horario):
    while lineup[horario-1][escenario-1] != '.':
            print(f'El horario {horario} y escenario {escenario} ya tiene un artista asignado')
            escenario = int(input("Ingresar escenario: "))
    return escenario

def validar_horario(horario, lineup, escenario):
    while lineup[horario-1][escenario-1] != '.':
            print(f'El horario {horario} y escenario {escenario} ya tiene un artista asignado')
            horario = int(input("Ingresar horario: "))
    return horario

def validar_horario_escenario(lineup, horario, escenario):
    while horario < 1 or horario > len(lineup) or escenario < 1 or escenario > len(lineup[0]):
        print(f'Horario o escenario inválido. Horario debe ser entre 1 y {len(lineup)}, escenario entre 1 y {len(lineup[0])}')
        horario = int(input("Elegir horario: "))
        escenario = int(input("Ingresar escenario: "))

    while lineup[horario-1][escenario-1] != '.':
        print(f'El horario {horario} y escenario {escenario} ya tiene un artista asignado')
        horario = int(input("Elegir horario: "))
        escenario = int(input("Ingresar escenario: "))

    return escenario, horario

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

    escenario, horario = validar_horario_escenario(lineup, horario, escenario)


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

def imprimir_grilla_con_nombres(lineup, horarios, escenarios, codigos, nombre_artistas):
    """
    Muestra la grilla reemplazando cada código de artista por su nombre,
    sin modificar la matriz original (lineup guarda códigos para el resto
    del programa). Reutiliza imprimir_grilla() para mantener exactamente
    el mismo formato de columnas y alineación.
    """
    copia = [fila[:] for fila in lineup]  # copia independiente, no afecta lineup

    for f in range(len(copia)):
        for c in range(len(copia[f])):
            if copia[f][c] in codigos:
                pos = codigos.index(copia[f][c])
                copia[f][c] = nombre_artistas[pos]

    imprimir_grilla(copia, horarios, escenarios)


def comprar_entradas(tot, venta_tot, entradas, tipo, vendidas_gen, vendidas_vip, max_operacion):
    """
    Registra una compra de entradas de tipo: General y VIP.
    Validad cantidad maxima por operacion y disponibilidad de las mismas antes de confirmar.
    Devuelve los acumuladores actualizados y ademas se agrega la operacion al registro de compras
    """
    print("\nIngresar entradas a comprar:\n")
    if tipo == 1:
        stock_restante = entradas[0][1] - vendidas_gen
    else:
        stock_restante = entradas[1][1] - vendidas_vip

    limite = min(max_operacion, stock_restante) 
    entradas_a_comprar = int(input())
    while entradas_a_comprar > limite:
        print("ERROR. No se pudo realizar la compra")
        entradas_a_comprar = int(input())

    importe = entradas_a_comprar * entradas[tipo - 1][0]
    tot += entradas_a_comprar
    venta_tot += importe

    if tipo == 1:
        vendidas_gen += entradas_a_comprar
    else:
        vendidas_vip += entradas_a_comprar


    return tot, venta_tot, vendidas_gen, vendidas_vip

def buscar_artista(buscado, codigos, nombre_artistas, lineup, escenarios, horarios):
    cods = [c.strip().lower() for c in codigos] # Para ignorar los espacios y las mayúsculas en los elementos dentro de la lista.
    nombres = [n.strip().lower() for n in nombre_artistas]

    if buscado in cods:
        indice = cods.index(buscado)
    elif buscado in nombres:
        indice = nombres.index(buscado)

    nombre_encontrado = nombre_artistas[indice]
    codigo_encontrado = codigos[indice]

    for f in range(len(lineup)):
        for c in range(len(lineup[f])):
            if lineup[f][c] == codigo_encontrado:
                escenario_encontrado = escenarios[c]
                horario_encontrado = horarios[f]

    return nombre_encontrado, escenario_encontrado, horario_encontrado


def calcular_disponibilidad_general(tot, capacidad):
    porcentaje_vendido = (tot/capacidad) *100
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


def cambiar_artista(lineup, codigos, indice, codigo_nuevo):
    codigo_viejo = codigos[indice]
    codigos[indice] = codigo_nuevo

    for fila in range(len(lineup)):
        for columna in range(len(lineup[fila])):
            if lineup[fila][columna] == codigo_viejo:
                lineup[fila][columna] = codigo_nuevo


def buscar_posicion_en_lineup(lineup, codigo):
    """
    Busca en la matriz lineup la posición (horario, escenario) del artista con el código dado.
    Retorna una tupla (horario, escenario) en base 1, o (None, None) si no está asignado.
    """
    for f in range(len(lineup)):
        for c in range(len(lineup[f])):
            if lineup[f][c] == codigo:
                return f + 1, c + 1
    return None, None

def imprimir_artistas_ordenados(nombre_artistas):
    artistas_ordenados = sorted(nombre_artistas, key=str.lower) # Usamos key ya que sorted no distingue bien mayúsculas y minúsculas.
    for a in range(len(artistas_ordenados)):
        print(f"★ {artistas_ordenados[a]}")

