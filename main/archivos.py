import json
import random
from json import load
from datetime import datetime
from validaciones import *


def leer_archivo():
    """
    Lee configuracion.json y retorna el diccionario de configuración ya validado.
    Si el archivo no se puede leer o su estructura es inválida, informa el error y retorna None.
    """
    try:
        with open("configuracion.json", 'rt', encoding='utf-8') as arch:
            config = load(arch)
    except OSError:
        print("ERROR. No se pudo leer el archivo configuracion.json")
        return None
    except ValueError:
        print("ERROR. configuracion.json tiene un formato inválido (revisar comas, comillas y llaves).")
        return None

    motivo = validar_configuracion(config)
    if motivo is not None:
        print(f"ERROR. configuracion.json es inválido: {motivo}.")
        return None
    return config

def verificar_login():
    """
    Verifica que login.txt se pueda leer y tenga al menos una cuenta Admin válida.
    Retorna True si está todo bien; si no, informa el error y retorna False.
    """
    try:
        cuentas = leer_cuentas()
    except (OSError, ValueError):
        print("[ERROR] No se encontró o no se pudo leer login.txt. El programa no puede iniciar sin ese archivo.")
        return False
    if not any(c[3] == "Admin" for c in cuentas):
        print("[ERROR] login.txt no contiene ninguna cuenta Admin válida.")
        return False
    return True

def repitencia_usuarios(nombre, mail):
    """
    Recibe un nombre de usuario y un mail.
    Retorna True si alguno de los dos ya está registrado en login.txt.
    """
    try:
        cuentas = leer_cuentas()
    except FileNotFoundError:
        print("ERROR: no se encontro login.txt")
        return False
    except (OSError, ValueError):
        print("Error al leer el archivo")
        return False
    return any(c[0].lower() == nombre.lower() or c[2].lower() == mail.lower() for c in cuentas)

def registrar_cuenta(nombre, contrasena, mail):
    """
    Recibe nombre, contraseña y mail ya validados.
    No retorna un valor; agrega la cuenta a login.txt con el rol 'Usuario'.
    Si el archivo no termina en salto de línea, lo agrega para no pegar la cuenta a la última línea.
    """
    try:
        prefijo = ""
        try:
            with open("login.txt", "rt", encoding="utf-8") as arch:
                contenido = arch.read()
            if contenido != "" and contenido[-1] != "\n":
                prefijo = "\n"
        except FileNotFoundError:
            pass  # si no existe, "at" lo crea

        with open("login.txt", "at", encoding="utf-8") as arch:
            arch.write(f"{prefijo}{nombre};{contrasena};{mail};Usuario\n")
        print("Usuario agregado con exito!")
    except (OSError, ValueError):
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
        for c in leer_cuentas():
            if c[0] == nombre:
                if c[1] == contrasena:
                    return c[3], None
                return None, causa[2]
        return None, causa[0]
    except FileNotFoundError:
        print("ERROR: no se encontro login.txt")
    except (OSError, ValueError):
        print("Error al leer el archivo")
    return None, causa[0]

def leer_logs():
    """
    Lee logs.json y retorna la lista de intentos válidos (diccionarios con 'user_ingresado' de tipo texto).
    Si el archivo no existe, no se puede leer o no tiene estructura de lista, retorna [].
    Los elementos con estructura incorrecta se ignoran.
    """
    try:
        with open("logs.json", mode="rt", encoding="utf-8") as arch:
            datos = load(arch)
    except FileNotFoundError:
        return []
    except (OSError, ValueError):
        print("[ERROR] No se pudo leer logs.json.")
        return []
    if not isinstance(datos, list):
        print("[ERROR] logs.json debe contener una lista de intentos.")
        return []
    return [i for i in datos if isinstance(i, dict) and isinstance(i.get("user_ingresado"), str)]

def logs_ilegibles():
    """Retorna True si logs.json existe pero no se puede interpretar como una lista."""
    try:
        with open("logs.json", mode="rt", encoding="utf-8") as arch:
            datos = load(arch)
    except FileNotFoundError:
        return False
    except (OSError, ValueError):
        return True
    return not isinstance(datos, list)

def intento_fallido(nombre, causa):
    """
    Recibe el usuario ingresado y la causa del fallo.
    No retorna un valor; agrega el intento a logs.json. La contraseña nunca se guarda.
    Si logs.json está dañado no lo sobrescribe, para no perder el historial.
    """
    if logs_ilegibles():
        print("[ERROR] logs.json está dañado. No se registró el intento para no perder el historial.")
        return
    intentos = leer_logs()
    intentos.append({
        "user_ingresado": nombre,
        "fecha": datetime.now().strftime("%d-%m-%Y"),
        "causa": causa
    })
    try:
        with open("logs.json", "wt", encoding="utf-8") as arch:
            json.dump(intentos, arch, indent=4, ensure_ascii=False)
    except OSError:
        print("Error al guardar el archivo")

def crear_reporte():
    """
    Lee logs.json y acumula la cantidad de intentos fallidos por usuario.
    Retorna el diccionario {usuario: cantidad}; queda vacío si no hay intentos o no se puede leer.
    """
    acumulador = {}
    for intento in leer_logs():
        usuario = intento["user_ingresado"]
        acumulador[usuario] = acumulador.get(usuario, 0) + 1
    return acumulador

def calcular_total(entradas, mostrar_avisos=False):
    """
    Recorre compras.csv y acumula cantidad y monto por tipo de entrada.
    Descarta (informando si mostrar_avisos) las filas inválidas o que superen el cupo máximo.
    Retorna la tupla (total_entradas, monto_total, total_general, total_vip).
    """
    ventas = {"general": {"cantidad": 0, "monto": 0},
              "vip": {"cantidad": 0, "monto": 0}}
    nombres = {"general": "General", "vip": "VIP"}
    ids_vistos = set()
    try:
        with open("compras.csv", mode='rt', encoding='utf-8') as arch:
            primera = arch.readline()
            inicio = 2
            if primera.strip() != "id;fecha;nombre_completo;mail;dni;tipo_entrada;cantidad;monto_final":
                if mostrar_avisos and primera != "":
                    print("[AVISO] compras.csv no tiene el encabezado esperado; se procesa desde la primera línea.")
                arch.seek(0)
                inicio = 1
            for nro, linea in enumerate(arch, start=inicio):
                if linea.strip() == "":
                    continue
                campos = linea.strip().split(';')
                datos, motivo = validar_fila_compra(campos, entradas)
                if datos is not None and campos[0].strip() in ids_vistos:
                    datos, motivo = None, "id repetido"
                if datos is not None:
                    tipo, cantidad, monto = datos
                    if ventas[tipo]["cantidad"] + cantidad > entradas[nombres[tipo]]["cupo_maximo"]:
                        datos, motivo = None, "supera el cupo máximo de ese tipo de entrada"
                if datos is None:
                    if mostrar_avisos:
                        print(f"[AVISO] Fila {nro} descartada ({motivo}): {linea.strip()}")
                    continue
                ids_vistos.add(campos[0].strip())
                ventas[tipo]["cantidad"] += cantidad
                ventas[tipo]["monto"] += monto
    except FileNotFoundError:
        pass
    except (OSError, ValueError):
        print("[ERROR] No se pudo leer compras.csv.")

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
        try:
            with open("compras.csv", "wt", encoding="utf-8") as arch:
                arch.write("id;fecha;nombre_completo;mail;dni;tipo_entrada;cantidad;monto_final\n")
        except OSError:
            print("[ERROR] No se pudo crear compras.csv.")

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
    except (OSError, ValueError):
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

def leer_cuentas():
    """
    Lee login.txt y retorna la lista de cuentas válidas [usuario, contraseña, mail, rol].
    Ignora el encabezado y las líneas con estructura incorrecta.
    Puede lanzar OSError / ValueError si no se puede leer el archivo.
    """
    cuentas = []
    with open("login.txt", "rt", encoding="utf-8") as arch:
        for linea in arch:
            campos = linea.strip().split(";")
            # El encabezado termina en "rol", que no es Admin ni Usuario, por eso se ignora.
            if len(campos) == 4 and campos[3] in ("Admin", "Usuario"):
                cuentas.append(campos)
    return cuentas