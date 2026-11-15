"""
 Dada una lista de números ordenada ascendentemente, desarrollar 
busqueda_binaria(datos, objetivo) que devuelva el índice del objetivo, o -1 si no está. No recorrer 
secuencialmente. Ejemplo: [2,5,8,11,16,20], valor 11 → 3. usar recursividad. No usar ciclos, ni funciones auxiliares con parámetros adicionales.
"""

def busqueda_binaria(datos, objetivo): #
    if len(datos) == 0:                # Caso base.
        return -1                      #
    else:
        medio = len(datos) // 2
        if datos[medio] == objetivo:
            return medio
        elif datos[medio] < objetivo:
            resultado = busqueda_binaria(datos[medio + 1:], objetivo) # Caso recursivo
            if resultado == -1:
                return -1
            else:
                return medio + 1 + resultado
        else:
            return busqueda_binaria(datos[:medio], objetivo) # Caso recursivo

print(busqueda_binaria([2,5,8,11,16,20], 11)) #una sola llamada recursiva

def prod_digitos(n):
    if n < 10:
        return n
    if n % 10 == 0:
        return 0
    return n % 10 * prod_digitos(n // 10)

print(prod_digitos(234))