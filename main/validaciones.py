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

def validar_dni():
    while True:
        dni = input("Ingresar DNI del responsable de la entrada: ").strip()
        if fullmatch(r"\d{7,8}", dni):
            return dni
        print("[ERROR] El DNI debe tener 7 u 8 dígitos, solo números y sin puntos (ej: 12345678).")


