"""
Diseñar es_palindromo(texto) para determinar si el texto se lee igual de 
izquierda a derecha que al revés. Ignorar espacios y diferencias entre mayúsculas y minúsculas. No 
invertir la cadena. Ejemplo: "Anita lava la tina" → True.
"""
def es_palindromo(texto):
    texto = texto.strip().lower()
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return es_palindromo(texto[1:-1])

print(es_palindromo("Anita lava la tina"))