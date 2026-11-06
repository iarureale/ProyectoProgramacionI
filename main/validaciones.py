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

    return fullmatch(r"A-[0-9]{2}", codigo) is not None

def es_cantidad_valida(texto):
    """
    Recibe el texto ingresado por el usuario.
    Retorna True si representa un número entero positivo.
    """
    return fullmatch(r"[0-9]+", texto) is not None and int(texto) > 0

'''
VALIDACIONES DEL SEGUNDO ALCANCE
'''

def es_usuario_valido(nombre):
    """
    Recibe el nombre de usuario.
    Retorna True si tiene entre 4 y 15 caracteres: letras, números o guion bajo.
    """
    return fullmatch(r"[A-Za-z0-9_]{4,15}", nombre) is not None

def es_mail_valido(mail):
    """
    Recibe el mail.
    Retorna True si tiene la estructura nombre@dominio.ext.
    """
    return fullmatch(r"[A-Za-z0-9]+([._+-][A-Za-z0-9]+)*@([A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}", mail) is not None

def es_dni_valido(dni):
    """
    Recibe el DNI.
    Retorna True si tiene 7 u 8 dígitos, solo números y sin puntos.
    """
    return fullmatch(r"[0-9]{7,8}", dni) is not None

def es_contrasena_valida(contrasena):
    """
    Recibe la contraseña.
    Retorna True si tiene al menos 4 caracteres, incluye un número y no contiene ';'.
    """
    return len(contrasena) >= 4 and any(c.isdigit() for c in contrasena) and ";" not in contrasena