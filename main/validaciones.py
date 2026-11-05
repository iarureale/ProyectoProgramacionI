from re import fullmatch

'''
VALIDACIONES DEL PRIMER ALCANCE
'''

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

def es_cantidad_valida(texto):
    """
    Recibe el texto ingresado por el usuario.
    Retorna True si representa un número entero positivo.
    """
    return texto.isdigit() and int(texto) > 0

'''
VALIDACIONES DEL SEGUNDO ALCANCE
'''

def es_usuario_valido(nombre):
    return fullmatch(r"[A-Za-z0-9_]{4,15}", nombre) is not None

def es_mail_valido(mail):
    return fullmatch(r"[A-Za-z0-9._+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}", mail) is not None

def es_dni_valido(dni):
    return fullmatch(r"[0-9]{7,8}", dni) is not None

def es_contrasena_valida(contrasena):
    return len(contrasena) >= 4 and any(c.isdigit() for c in contrasena) and ";" not in contrasena


