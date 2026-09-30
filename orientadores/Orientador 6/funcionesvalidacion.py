import re

def validar_legajo(legajo):
    return re.fullmatch(r"[0-9]{5}", legajo) is not None


def validar_codigo(codigo):
    return re.fullmatch(r"[A-Z]{2}[0-9]{4}", codigo) is not None


def validar_telefono(telefono):
    return re.fullmatch(r"[0-9]{4}-[0-9]{4}", telefono) is not None


def validar_correo(correo):
    return re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", correo) is not None


def validar_importe(importe):
    return re.fullmatch(r"\$[0-9]+", importe) is not None


def validar_patente(patente):
    return re.fullmatch(r"[A-Z]{3}[0-9]{3}|[A-Z]{2}[0-9]{3}[A-Z]{2}", patente) is not None


def mostrar_resultados(nombre, funcion, cadenas):
    print(f"--- {nombre} ---")
    for cadena in cadenas:
        if funcion(cadena):
            print(f'La cadena "{cadena}" coincide con el patrón.')
        else:
            print(f'La cadena "{cadena}" no coincide con el patrón.')
    print()


legajos = ["12345", "00001", "99999", "1234", "123456", "12a45", ""]
codigos = ["AB1234", "ZZ0000", "MC9999", "ab1234", "A12345", "ABC123", ""]
telefonos = ["1234-5678", "0000-0000", "4321-8765", "12345678", "123-45678", "abcd-efgh", ""]
correos = ["iaru@dominio.com", "sol@dominio.com", "a.b_c@dom.ar", "iara@", "@dominio.com", "sol@dominio.c", ""]
importes = ["$1", "$100", "$007", "100", "$", "$12.5", ""]
patentes = ["ABC123", "AB123CD", "ZZZ999", "AB1234", "abc123", "ABC12", ""]

mostrar_resultados("validar_legajo", validar_legajo, legajos)
mostrar_resultados("validar_codigo", validar_codigo, codigos)
mostrar_resultados("validar_telefono", validar_telefono, telefonos)
mostrar_resultados("validar_correo", validar_correo, correos)
mostrar_resultados("validar_importe", validar_importe, importes)
mostrar_resultados("validar_patente", validar_patente, patentes)
