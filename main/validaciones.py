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

def validar_fila_compra(campos, entradas):
    """
    Recibe los campos de una fila de compras.csv (lista) y la configuración de entradas.
    Retorna ((tipo, cantidad, monto), None) si la fila es válida,
    o (None, motivo) si no lo es.
    """
    if len(campos) != 8:
        return None, "cantidad de columnas incorrecta"

    _, _, _, mail, dni, tipo, texto_cantidad, texto_monto = [c.strip() for c in campos]
    tipo = tipo.lower()

    if tipo not in ("general", "vip"):
        return None, f"tipo de entrada '{tipo}' inexistente"
    datos_tipo = entradas["General" if tipo == "general" else "VIP"]

    if not es_cantidad_valida(texto_cantidad):
        return None, "cantidad inválida (debe ser un entero positivo)"
    cantidad = int(texto_cantidad)
    if cantidad > datos_tipo["max_operacion"]:
        return None, f"la cantidad supera el máximo por operación ({datos_tipo['max_operacion']})"

    try:
        monto = float(texto_monto)
    except ValueError:
        return None, "monto no numérico"
    if monto != cantidad * datos_tipo["precio"]: 
        return None, "el monto no coincide con cantidad x precio"

    if not es_dni_valido(dni):
        return None, "DNI inválido"
    if not es_mail_valido(mail):
        return None, "mail inválido"

    return (tipo, cantidad, monto), None

def validar_configuracion(config):
    """
    Recibe lo cargado desde configuracion.json.
    Retorna None si la estructura es válida, o un texto con el motivo del error.
    """
    if not isinstance(config, dict):
        return "el archivo debe contener un objeto JSON ({ ... })"
    for clave in ("escenarios", "horarios", "entradas"):
        if clave not in config:
            return f"falta la clave '{clave}'"

    for clave, cantidad in (("escenarios", 5), ("horarios", 8)):
        lista = config[clave]
        if not (isinstance(lista, list) and len(lista) == cantidad and all(isinstance(x, str) and x.strip() for x in lista)):
            return f"'{clave}' debe ser una lista de {cantidad} textos no vacíos"

    if not isinstance(config["entradas"], dict):
        return "'entradas' debe ser un objeto con 'General' y 'VIP'"
    for tipo in ("General", "VIP"):
        datos = config["entradas"].get(tipo)
        if not isinstance(datos, dict):
            return f"falta la entrada '{tipo}'"
        for campo in ("precio", "cupo_maximo", "max_operacion"):
            valor = datos.get(campo)
            if isinstance(valor, bool) or not isinstance(valor, (int, float)) or not (0 < valor < float("inf")): # Verificar que no entran valores raros como Infinity o NaN
                return f"'{tipo}' -> '{campo}' debe ser un número positivo"
        if not isinstance(datos["cupo_maximo"], int) or not isinstance(datos["max_operacion"], int):
            return f"'{tipo}' -> 'cupo_maximo' y 'max_operacion' deben ser enteros"
    return None