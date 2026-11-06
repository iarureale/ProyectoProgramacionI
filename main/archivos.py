import json
import random
from json import load
from datetime import datetime
from validaciones import *


def leer_archivo():
    """
    Lee configuracion.json y retorna el diccionario de configuración.
    Si el archivo no se puede leer o tiene un formato inválido, informa el error
    y retorna None.
    """
    config = None
    try:
        with open("configuracion.json", 'rt', encoding='utf-8') as arch:
            config = load(arch)
    except OSError:
        print("ERROR. No se pudo leer el archivo")
    except ValueError:
        print("ERROR. configuracion.json tiene un formato inválido (revisar comas, comillas y llaves).")
    if config is not None:
        for clave in ("escenarios", "horarios", "entradas"):
            if clave not in config:
                print(f"ERROR. configuracion.json no tiene la clave '{clave}'.")
                return None
    return config

def verificar_login():
    """
    Verifica que login.txt exista y se pueda abrir (es un archivo obligatorio).
    Retorna True si está disponible; si no, informa el error y retorna False.
    """
    try:
        with open("login.txt", "rt", encoding="utf-8"):
            return True
    except OSError:
        print("[ERROR] No se encontró login.txt. El programa no puede iniciar sin ese archivo.")
        return False

def repitencia_usuarios(nombre, mail):
    """
    Recibe un nombre de usuario y un mail.
    Recorre login.txt y retorna True si alguno de los dos ya está registrado.
    """
    try:
        with open("login.txt", "rt", encoding="utf-8") as arch:
            arch.readline()
            for linea in arch:
                campos = linea.strip().split(";")
                if len(campos) == 4 and (campos[0].lower() == nombre.lower() or campos[2].lower() == mail.lower()):
                    return True
    except FileNotFoundError:
        print("ERROR: no se encontro login.txt")
    except OSError:
        print("Error al leer el archivo")
    return False

def registrar_cuenta(nombre, contrasena, mail):
    """
    Recibe nombre, contraseña y mail ya validados.
    No retorna un valor; agrega la cuenta a login.txt con el rol 'Usuario'.
    """
    try:
        with open("login.txt", "at", encoding="utf-8") as arch:
            arch.write(f"{nombre};{contrasena};{mail};Usuario\n")
        print("Usuario agregado con exito!")
    except OSError:
        print("Error al acceder al archivo")

def buscar_usuarios(nombre, contrasena):
    """
    Recibe el nombre de usuario y la contraseña ingresados.
    Retorna una tupla (rol, None) si las credenciales son correctas, o (None, causa)
    con el motivo del fallo: formato incorrecto, usuario no encontrado o campos que no coinciden.
    """
    causa = ("Usuario no encontrado.", "Usuario con formato incorrecto.",  "Los campos no coinciden.")
    if not es_usuario_valido(nombre):
        return None, causa[1]
    try:
        with open("login.txt", "rt", encoding="utf-8") as arch:
            lineas = arch.readlines()
            for linea in lineas[1:]:  #IGNORO LA PRIMERA LINEA PQ SINO ME TIRA SIEMPRE USUARIO NO ENCONTRADO
                if not linea.strip():
                    continue

                campos = linea.strip().split(";")
                if len(campos) == 4 and campos[0] == nombre:
                    if campos[1] == contrasena:
                        return campos[3], None
                    return None, causa[2]
        return None, causa[0]
    except FileNotFoundError:
        print("ERROR: no se encontro login.txt")
    except OSError:
        print("Error al leer el archivo")
    return None, causa[0]

def intento_fallido(nombre, causa):
    """
    Recibe el usuario ingresado y la causa del fallo.
    No retorna un valor; agrega el intento (usuario, fecha y causa) a la lista de logs.json.
    La contraseña ingresada nunca se guarda.
    """

    ingreso_fallido ={
    "user_ingresado": nombre,
    "fecha": datetime.now().strftime("%d-%m-%Y"),
    "causa": causa
    }
    try:
        with open("logs.json", "rt", encoding="utf-8") as arch:
            intentos = json.load(arch)
    except (OSError, ValueError):
        intentos = []
    intentos.append(ingreso_fallido)
    try:
        with open("logs.json", "wt", encoding="utf-8") as arch:
            json.dump(intentos, arch, indent=4, ensure_ascii=False)
    except OSError:
        print("Error al guardar el archivo")

def calcular_total(mostrar_avisos=False):
    """
    Recorre compras.csv y acumula cantidad y monto en un diccionario por tipo de entrada.
    Retorna la tupla (total_entradas, monto_total, total_general, total_vip).
    Las filas con formato incorrecto se informan sin perder las válidas.
    """
    ventas = {"general": {"cantidad": 0, "monto": 0},
              "vip": {"cantidad": 0, "monto": 0}}
    try:
        with open("compras.csv", mode='rt', encoding='utf-8') as arch:
            arch.readline()
            for lineas in arch:
                if lineas.strip() == "":
                    continue
                campos = lineas.strip().split(';')
                try:
                    cantidad = int(campos[6])
                    monto = float(campos[7])
                    ventas[campos[5]]["cantidad"] += cantidad
                    ventas[campos[5]]["monto"] += monto
                except (IndexError, ValueError, KeyError):
                    if mostrar_avisos:
                        print(f"[AVISO] Fila con formato incorrecto: {lineas.strip()}")
    except FileNotFoundError:
        pass

    tot_gen = ventas["general"]["cantidad"]
    tot_vip = ventas["vip"]["cantidad"]
    monto_total = ventas["general"]["monto"] + ventas["vip"]["monto"]
    return tot_gen + tot_vip, monto_total, tot_gen, tot_vip

def crear_compras_si_no_existe():
    """
    Crea compras.csv con su encabezado si todavía no existe.
    Crea el encabezado también si el archivo está vacío.
    No retorna un valor.
    """
    try:
        with open("compras.csv", "rt", encoding="utf-8") as arch:
            tiene_datos = arch.readline() != ""
    except FileNotFoundError:
        tiene_datos = False
    if not tiene_datos:
        with open("compras.csv", "wt", encoding="utf-8") as arch:
            arch.write("id;fecha;nombre_completo;mail;dni;tipo_entrada;cantidad;monto_final\n")

def chequear_id():
    """
    Genera un id aleatorio de 4 dígitos que no esté repetido en compras.csv.
    Retorna el id generado.
    """
    crear_compras_si_no_existe()
    id = random.randint(1000,9999)
    repetido = True
    try:
        with open('compras.csv', mode='rt', encoding='utf-8') as arch:
            while repetido:
                repetido = False
                arch.seek(0) #Nos permite volver al principio sin abrir varias veces un archivo
                for lineas in arch:
                    campos = lineas.strip().split(';')
                    if campos[0] == str(id):
                        repetido = True
                        id = random.randint(1000,9999)
                        break
    except FileNotFoundError:
        pass
    return id

def guardar_compra(tipo_entrada, cantidad, precio_general, precio_vip, nombre_completo, mail, dni):
    """
    Recibe el tipo de entrada (1 = general, 2 = vip), la cantidad, los precios y los datos
    del comprador ya validados. Calcula el monto final y agrega la compra a compras.csv.
    Retorna True si se guardó, o False si hubo un error de escritura.
    """
    id = chequear_id()
    fecha = datetime.today().strftime("%d-%m-%Y")
    if tipo_entrada == 1:
        tipo, monto_final = 'general', cantidad * precio_general
    else:
        tipo, monto_final = 'vip', cantidad * precio_vip
    try:
        with open('compras.csv', mode='at', encoding='utf-8') as arch:
            arch.write(f"{id};{fecha};{nombre_completo};{mail};{dni};{tipo};{cantidad};{monto_final}\n")
        return True
    except OSError:
        print("El archivo tuvo un error al intentar procesarlo, porfavor revisar.")
        return False

def crear_reporte():
    """
    Lee logs.json y acumula en un diccionario la cantidad de intentos fallidos por usuario.
    Retorna el diccionario {usuario: cantidad}; queda vacío si no hay intentos o no se puede leer el archivo.
    """
    acumulador = {}

    try:
        with open("logs.json", mode="rt", encoding="utf-8") as arch:
            intentos = load(arch)
    except FileNotFoundError:
        return acumulador
    except (OSError, ValueError):
        print("[ERROR] No se pudo leer logs.json.")
        return acumulador

    for intento in intentos:
        usuario = intento.get("user_ingresado")
        if usuario is not None:
            acumulador[usuario] = acumulador.get(usuario, 0) + 1
    return acumulador