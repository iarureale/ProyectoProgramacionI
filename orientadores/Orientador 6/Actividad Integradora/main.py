import formularioregistro

def pedir_nombre():
    while True:
        nombre = input("Nombre y apellido: ")
        if formularioregistro.validar_nombre(nombre):
            return nombre
        print("Nombre inválido. Use solo letras y espacios. Ej: Iara Reale")


def pedir_legajo():
    while True:
        legajo = input("Legajo: ")
        if formularioregistro.validar_legajo(legajo):
            return legajo
        print("Legajo inválido. Debe tener exactamente 7 dígitos. Ej: 1234567")


def pedir_correo():
    while True:
        correo = input("Correo electrónico: ")
        if formularioregistro.validar_correo(correo):
            return correo
        print("Correo inválido. Formato usuario@dominio.ext. Ej: ireale@dominio.com")


def pedir_telefono():
    while True:
        telefono = input("Teléfono: ")
        if formularioregistro.validar_telefono(telefono):
            return telefono
        print("Teléfono inválido. Formato 4 dígitos-4 dígitos. Ej.: 1234-5678")


def pedir_comision():
    while True:
        comision = input("Código de comisión: ")
        if formularioregistro.validar_comision(comision):
            return comision
        print("Comisión inválida. Año (1 a 3), turno (M, T o N) y 2 dígitos. Ej.: 2T03")


def mostrar_datos(nombre, legajo, correo, telefono, comision):
    print("\n--- Datos registrados ---")
    print(f"Nombre: {nombre}")
    print(f"Legajo: {legajo}")
    print(f"Correo electrónico: {correo}")
    print(f"Teléfono: {telefono}")
    print(f"Código de comisión: {comision}")


#Programa Principal
print("--- Formulario de registro ---")
nombre = pedir_nombre()
legajo = pedir_legajo()
correo = pedir_correo()
telefono = pedir_telefono()
comision = pedir_comision()

mostrar_datos(nombre, legajo, correo, telefono, comision)