from archivos import *
from validaciones import *



def pedir_opcion_valida(mensaje, opciones_validas):
    """
    Recibe el mensaje a mostrar y la lista de opciones validas (ej: [1, 2, 3]).
    Retorna la opcion ingresada como entero, solicitandola nuevamente mientras
    no sea un numero dentro de las opciones validas.
    """
    opcion = input(mensaje)

    while not opcion.isdigit() or int(opcion) not in opciones_validas:
        print('\n[ERROR] Opción inválida. Por favor, seleccione una opción disponible.')
        opcion = input(mensaje)

    return int(opcion)

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
    """
    Recibe el escenario elegido, la matriz lineup y el horario ya definido.
    Retorna un escenario valido: si la combinacion horario/escenario ya esta ocupada,
    solicita un nuevo escenario hasta encontrar uno disponible.
    """
    while lineup[horario-1][escenario-1] != '.':
            print(f'[AVISO] El horario {horario} y el escenario {escenario} ya tienen un artista asignado')
            escenario = pedir_opcion_valida("Ingresar escenario: ", [1, 2, 3, 4, 5])
    return escenario

def validar_horario(horario, lineup, escenario):
    """
    Recibe el horario elegido, la matriz lineup y el escenario ya definido.
    Retorna un horario valido: si la combinacion horario/escenario ya esta ocupada,
    solicita un nuevo horario hasta encontrar uno disponible.
    """
    while lineup[horario-1][escenario-1] != '.':
            print(f'[AVISO] El horario {horario} y el escenario {escenario} ya tienen un artista asignado')
            horario = pedir_opcion_valida("Ingresar horario: ", [1, 2, 3, 4, 5, 6, 7, 8])
    return horario

def validar_horario_escenario(lineup, horario, escenario):
    """
    Recibe la matriz lineup, y el horario/escenario propuestos.
    Retorna la tupla (escenario, horario) validada: solicita nuevos valores mientras esten fuera de rango o mientras la combinacion ya tenga un artista asignado.
    """

    while lineup[horario-1][escenario-1] != '.':
        print(f'[AVISO] El horario {horario} y el escenario {escenario} ya tienen un artista asignado.')
        horario = pedir_opcion_valida("Ingresar horario: ", [1, 2, 3, 4, 5, 6, 7, 8])
        escenario = pedir_opcion_valida("Ingresar escenario: ", [1, 2, 3, 4, 5])

    return escenario, horario

def ingresar_codigo():
    """
    Solicita por teclado el código del artista y valida que cumpla con el formato 'A-XX'.
    Retorna el código validado en mayúsculas.
    """
    codigo = input("Ingresar codigo del artista a registrar: ").upper()
    while not validar_codigo(codigo):
        print("[ERROR] Código inválido. Por favor, ingrese un código con el formato 'A-XX'.")
        codigo = input("Ingresar código del artista a registrar: ").upper()
    return codigo


def ingresar_artista(lineup, nombre_artistas, codigos, horarios, escenarios):
    """
    Recibe la matriz lineup, las listas de nombres y codigos de artistas, y las tuplas de horarios y escenarios.
    No retorna un valor; solicita por teclado el codigo, nombre, horario y escenario del nuevo artista,
    valida los datos y actualiza la matriz y las listas correspondientes.
    """
    if len(codigos) >= 30:
        print("[AVISO] No se pueden ingresar más artistas: ya se alcanzó el límite de 30 artistas registrados.")
        return
    
    codigo = ingresar_codigo()

    while artista_ya_ingresado(codigo, codigos):
        print(f'[AVISO] El código {codigo} ya está ingresado en el lineup. Por favor, ingrese uno distinto.')
        codigo = ingresar_codigo()

    codigos.append(codigo)
    nombre_artistico = input("Ingresar nombre del artista: ")
    while nombre_artistico == "" or nombre_artistico.isspace():
        print("[ERROR] El nombre no puede quedar vacío ni contener únicamente espacios en blanco.")
        nombre_artistico = input("Ingresar nombre del artista: ")

    nombre_artistas.append(nombre_artistico)

    print("\nHorarios disponibles:")
    for i in range(len(horarios)):
        print(f'{i+1}. {horarios[i]}')
    horario = pedir_opcion_valida("Ingresar horario: ", [1, 2, 3, 4, 5, 6, 7, 8])

    print("\nEscenarios disponibles:")
    for i in range(len(escenarios)):
        print(f'{i+1}. {escenarios[i]}')
    escenario = pedir_opcion_valida("Ingresar escenario: ", [1, 2, 3, 4, 5])

    escenario, horario = validar_horario_escenario(lineup, horario, escenario)

    lineup[horario-1][escenario-1] = codigo

    print(f'El artista con código {codigo} fue asignado correctamente al horario {horario} y al escenario {escenario}.')

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
            valor = lineup[f][c]
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

def calcular_limite_compra(tipo, entradas, vendidas_gen, vendidas_vip):
    """
    Recibe el tipo de entrada, la configuración de entradas y lo vendido hasta ahora.
    Retorna la cantidad máxima permitida en esta operación.
    """
    vendidas = vendidas_gen if tipo == 1 else vendidas_vip
    nombre = "General" if tipo == 1 else "VIP"
    stock_restante = entradas[nombre]["cupo_maximo"] - vendidas
    return min(entradas[nombre]["max_operacion"], stock_restante)


def buscar_artista(buscado, codigos, nombre_artistas, lineup, escenarios, horarios):
    """
    Recibe el codigo o nombre buscado, las listas de codigos y nombres, la matriz y las tuplas de escenarios y horarios.
    Retorna una tupla (nombre, escenario, horario) del artista encontrado.
    """
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
    """
    Recibe la cantida total de entradas vendidas y la capacidad correspondiente.
    Retorna el porcentaje de disponibilidad restante sobre esa capacidad.
    """
    porcentaje_vendido = (tot/capacidad) *100
    capacidad_general = 100 - porcentaje_vendido
    return capacidad_general


def cambiar_artista(lineup, codigos, indice, codigo_nuevo):
    """
    Recibe la matriz lineup, la lista de codigos, el indice del artista a modificar y el nuevo codigo a asignar.
    No retorna un valor; actualiza el codigo del artista en la lista y en la matriz.
    """
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
    """
    Recibe la lista de nombres de artistas.
    No retorna un valor; nos muestra en pantalla los nombres ordenados alfabeticamente.
    """
    artistas_ordenados = sorted(nombre_artistas, key=str.lower) # Usamos key ya que sorted no distingue bien mayúsculas y minúsculas.
    for a in range(len(artistas_ordenados)):
        print(f"★  {artistas_ordenados[a]}")

def chequear_artista(lineup, modificar):
    '''
    Recorre toda la matriz para encontrar el escenario del artista y despues recorre los horarios para verificar si hay lugar libre.
    Retorna una bandera booleana si hay lugar libre.
    '''
    for f in range(len(lineup)):
        for c in range(len(lineup[f])):
            if lineup[f][c] == modificar:
                escenario = c
    libres = 0
    for f in range(len(lineup)):
        if lineup[f][escenario] == '.':
            libres += 1

    if libres == 0:
        print("\n[AVISO]Todos los horarios del escenario están ocupados.")
        return False
    else:
        return True

def contar_artistas_escenario(lineup, escenarios):
    """
    Recibe la matriz lineup y la tupla de escenarios.
    Retorna una lista con la cantidad de artistas asignados a cada escenario (mismo orden que escenarios).
    """
    conteo = [0] * len(escenarios)

    for f in range(len(lineup)):
        for c in range(len(lineup[f])):
            if lineup[f][c] != ".":
                conteo[c] += 1
    return conteo

'''
<======================FUNCIONES AGREGADAS EN LA SEGUNDA ETAPA===========================>

En validaciones.py: Validaciones de formato (expresiones regulares) y de datos ingresados.

En archivos.py: login.txt, configuracion.json, logs.json y compras.csv.
'''

def validacion_nombre():
    """
    Solicita por teclado el nombre de la cuenta hasta que cumpla es_usuario_valido.
    Retorna el nombre validado.
    """
    while True:
        nombre = input("Ingresar nombre de la cuenta (4 a 15 caracteres: letras, numeros o _): ").strip()
        if es_usuario_valido(nombre):
            return nombre
        print("[ERROR] El nombre de usuario debe tener entre 4 y 15 caracteres: letras, números o guion bajo (_).")

def validacion_contrasena():
    """
    Solicita por teclado la contraseña hasta que cumpla es_contrasena_valida.
    Retorna la contraseña validada.
    """
    mensaje = "Ingresar contraseña. Debe contener un numero y 4 caracteres: "
    contrasena = input(mensaje)
    while not es_contrasena_valida(contrasena):
        if ";" in contrasena:
            print("[ERROR] La contraseña no puede contener el carácter ';'.")
        else:
            print("[ERROR] La contraseña debe tener al menos 4 caracteres e incluir al menos un número.")
        contrasena = input(mensaje)
    return contrasena

def validacion_mail():
    """
    Solicita por teclado el mail hasta que cumpla es_mail_valido.
    Retorna el mail validado.
    """
    mail = input("Ingresá tu mail: ").strip()
    while not es_mail_valido(mail):
        print("[ERROR] El mail debe tener el formato usuario@dominio.com (ej: nombre@gmail.com).")
        mail = input("Ingresá tu mail: ").strip()
    return mail

def validar_dni():
    """
    Solicita por teclado el DNI del responsable hasta que cumpla es_dni_valido.
    Retorna el DNI validado.
    """
    dni = input("Ingresar DNI del responsable de la entrada: ").strip()
    while not es_dni_valido(dni):
        print("[ERROR] El DNI debe tener 7 u 8 dígitos, solo números y sin puntos (ej: 12345678).")
        dni = input("Ingresar DNI del responsable de la entrada: ").strip()
    return dni

def procesar_compra(tipo_entrada, cantidad, precio_general, precio_vip):
    """Pide los datos del comprador y los guarda con guardar_compra (archivos.py)."""
    nombre = input("Ingresar nombre del responsable de la entrada: ").strip()
    while nombre == "" or ";" in nombre:
        print("[ERROR] El nombre no puede estar vacío ni contener ';'.")
        nombre = input("Ingresar nombre del responsable de la entrada: ").strip()
    mail = validacion_mail()
    dni = validar_dni()
    return guardar_compra(tipo_entrada, cantidad, precio_general, precio_vip, nombre, mail, dni)