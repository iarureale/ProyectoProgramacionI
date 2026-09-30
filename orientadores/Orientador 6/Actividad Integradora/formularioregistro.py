import re

def validar_nombre(nombre):
    return re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombre) is not None

def validar_legajo(legajo):
    return re.fullmatch(r"[0-9]{7}", legajo) is not None

def validar_correo(correo):
    return re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", correo) is not None

def validar_telefono(telefono):
    return re.fullmatch(r"[0-9]{4}-[0-9]{4}", telefono) is not None

def validar_comision(comision):
    return re.fullmatch(r"[1-3][MTN][0-9]{2}", comision) is not None

