"""
4. Inversión de una cadena. Crear invertir(texto) que devuelva los caracteres en orden inverso, sin 
ciclos ni [::-1]. Ejemplo: invertir("python") → "nohtyp". Incluir el caso de cadena vacía.
"""

def invertir(texto):
    if texto == '':
        return ''
    if len(texto) == 0:
        return ''
    else:
        return texto[-1] + invertir(texto[:-1])

print(invertir("hola"))