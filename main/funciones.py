import json
from re import fullmatch
from json import load
from datetime import datetime
import random
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


def es_cantidad_valida(texto):
    """
    Recibe el texto ingresado por el usuario.
    Retorna True si representa un número entero positivo.
    """
    return texto.isdigit() and int(texto) > 0

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

FUNCIONES AGREGADAS EN LA SEGUNDA ETAPA

'''

def validacion_nombre():
    while True:
        nombre = input("Ingresar nombre de la cuenta (4 a 15 caracteres: letras, numeros o _): ").strip()
        if fullmatch(r"[A-Za-z0-9_]{4,15}", nombre):
            return nombre
        print("[ERROR] El nombre de usuario debe tener entre 4 y 15 caracteres: letras, números o guion bajo (_).")

def validacion_contrasena():
    contrasena = input("Ingresar contraseña. Debe contener un numero y 4 caracteres: ")

    while len(contrasena) < 4 or not any(c.isdigit() for c in contrasena) or ";" in contrasena: #Recorre la string en busca de numeros
        if ';' in contrasena:
            print("[ERROR] La contraseña no puede contener el carácter ';'.")
            contrasena = input("Ingresar contraseña. Debe contener un numero y 4 caracteres: ")
        else:
            print("[ERROR] La contraseña debe tener al menos 4 caracteres e incluir al menos un número.")
            contrasena = input("Ingresar contraseña. Debe contener un numero y 4 caracteres: ")
    return contrasena

def validacion_mail():
    patron = r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$"

    mail = input("Ingresá tu mail: ").strip()

    while not fullmatch(patron, mail):
        print("[ERROR] El mail debe tener el formato usuario@dominio.com (ej: nombre@gmail.com).")
        mail = input("Ingresá tu mail: ").strip()

    return mail

def repitencia_usuarios(nombre, mail):
    try:
        with open("login.txt", "rt", encoding="utf-8") as arch:
            arch.readline()
            for linea in arch:
                campos = linea.strip().split(";")
                if len(campos) == 4 and (campos[0] == nombre or campos[2] == mail):
                    return True
    except FileNotFoundError:
        print("ERROR: no se encontro login.txt")
    except OSError:
        print("Error al leer el archivo")
    return False

def registrar_cuenta(nombre, contrasena, mail):
    try:
        with open("login.txt", "at", encoding="utf-8") as arch:
            arch.write(f"{nombre};{contrasena};{mail};Usuario\n")
        print("Usuario agregado con exito!")
    except OSError:
        print("Error al acceder al archivo")

def buscar_usuarios(nombre, contrasena):
    causa = ("Usuario no encontrado.", "Usuario con formato incorrecto.",  "Los campos no coinciden.")
    if not fullmatch(r"[A-Za-z0-9_]{4,15}", nombre):
        return None, causa[1]
    try:
        with open("login.txt", "rt", encoding="utf-8") as arch:
            lineas = arch.readlines()
            for linea in lineas[1:]:  #IGNORO LA PRIMERA LINEA PQ SINO ME TIRA SIEMPRE USUARIO NO ENCONTRADO
                campos = linea.strip().split(";")
                if len(campos) == 4 and campos[0] == nombre:
                    if campos[1] == contrasena:
                        return campos[3], None
                    return None, causa[2]
    except FileNotFoundError:
        print("ERROR: no se encontro login.txt")
    except OSError:
        print("Error al leer el archivo")
    return None, causa[0]

def leer_archivo():
    config = None
    try:
        with open("configuracion.json", 'rt', encoding='utf-8') as arch:
            config = load(arch)
    except OSError:
        print("ERROR. No se pudo leer el archivo")
    return config

def intento_fallido(nombre, causa):

    ingreso_fallido ={
    "user_ingresado": nombre,
    "fecha": datetime.now().strftime("%d-%m-%Y"),
    "causa": causa
    }
    try:
        with open("logs.json", "rt", encoding="utf-8") as arch:
            intentos = json.load(arch)
    except:
        intentos = []
    intentos.append(ingreso_fallido)
    try:
        with open("logs.json", "wt", encoding="utf-8") as arch:
            json.dump(intentos, arch, indent=4, ensure_ascii=False)
    except OSError:
        print("Error al guardar el archivo")


def calcular_total():
    ventas = {"general": {"cantidad": 0, "monto": 0},
              "vip": {"cantidad": 0, "monto": 0}}
    try:
        with open("compras.csv", mode='rt') as arch:
            arch.readline()
            for lineas in arch:
                campos = lineas.strip().split(';')
                try:
                    ventas[campos[5]]["cantidad"] += int(campos[6])
                    ventas[campos[5]]["monto"] += float(campos[7])
                except (IndexError, ValueError, KeyError):
                    print(f"[AVISO] Fila con formato incorrecto: {lineas.strip()}")
    except FileNotFoundError:
        pass

    tot_gen = ventas["general"]["cantidad"]
    tot_vip = ventas["vip"]["cantidad"]
    monto_total = ventas["general"]["monto"] + ventas["vip"]["monto"]
    return tot_gen + tot_vip, monto_total, tot_gen, tot_vip


def chequear_id():
    id = random.randint(1000,9999)
    repetido = True
    with open('compras.csv', mode='rt') as arch:
        while repetido:
            repetido = False
            arch.seek(0) #Nos permite volver al principio sin abrir varias veces un archivo
            for lineas in arch:
                campos = lineas.strip().split(';')
                if campos[0] == str(id):
                    repetido = True
                    id = random.randint(1000,9999)
                    break
    return id


def validar_dni():
    while True:
        dni = input("Ingresar DNI del responsable de la entrada: ").strip()
        if fullmatch(r"\d{7,8}", dni):
            return dni
        print("[ERROR] El DNI debe tener 7 u 8 dígitos, solo números y sin puntos (ej: 12345678).")


def procesar_compra(tipo_entrada, cantidad, precio_general, precio_vip):
    #id;fecha;nombre_completo;mail;dni;tipo_entrada;cantidad;monto_final
    id = chequear_id()
    fecha = datetime.today().strftime("%d-%m-%Y")
    nombre_completo = input("Ingresar nombre del responsable de la entrada: ").strip()
    while nombre_completo == "" or ";" in nombre_completo:
            print("[ERROR] El nombre no puede estar vacío ni contener ';'.")
            nombre_completo = input("Ingresar nombre del responsable de la entrada: ").strip()
    mail = validacion_mail()
    dni = validar_dni()

    if tipo_entrada == 1:
        tipo= 'general'
        monto_final = cantidad * precio_general
    elif tipo_entrada == 2:
        tipo = 'vip'
        monto_final = cantidad * precio_vip
    try:
        with open('compras.csv', mode='at') as arch:
            arch.write(f"{id};{fecha};{nombre_completo};{mail};{dni};{tipo};{cantidad};{monto_final}\n")
        return True
    except OSError:
        print("El archivo tuvo un error al intentar procesarlo, porfavor revisar.")
        return False


