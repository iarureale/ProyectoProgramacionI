"""Validar una contraseña."""

def clave_valida(clave):
    tiene_numero = False
    for caracter in clave:
        if caracter.isdigit():
            tiene_numero = True
    return len(clave) >= 8 and tiene_numero
