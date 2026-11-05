import json
import random
from json import load
from re import fullmatch
from datetime import datetime
from validaciones import *


def leer_archivo():
    config = None
    try:
        with open("configuracion.json", 'rt', encoding='utf-8') as arch:
            config = load(arch)
    except OSError:
        print("ERROR. No se pudo leer el archivo")
    except ValueError:
        print("ERROR. configuracion.json tiene un formato inválido (revisar comas, comillas y llaves).")
    return config

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
    if not es_usuario_valido(nombre):
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

def intento_fallido(nombre, causa):

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

def calcular_total():
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
                    print(f"[AVISO] Fila con formato incorrecto: {lineas.strip()}")
    except FileNotFoundError:
        pass

    tot_gen = ventas["general"]["cantidad"]
    tot_vip = ventas["vip"]["cantidad"]
    monto_total = ventas["general"]["monto"] + ventas["vip"]["monto"]
    return tot_gen + tot_vip, monto_total, tot_gen, tot_vip

def crear_compras_si_no_existe():
    try:
        open("compras.csv", "rt", encoding="utf-8").close()
    except FileNotFoundError:
        with open("compras.csv", "wt", encoding="utf-8") as arch:
            arch.write("id;fecha;nombre_completo;mail;dni;tipo_entrada;cantidad;monto_final\n")

def chequear_id():
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

def verificar_login():
    try:
        with open("login.txt", "rt", encoding="utf-8"):
            return True
    except OSError:
        print("[ERROR] No se encontró login.txt. El programa no puede iniciar sin ese archivo.")
        return False