"""
6. Conversión decimal a binario. Programar a_binario(n) para un entero natural, devolviendo su 
representación binaria como cadena y sin utilizar bin(). Ejemplo: a_binario(13) → "1101". Considerar 
n=0. UTILIZANDO RECURSIVIDAD. No usar ciclos, conversión a string, funciones auxiliares con parámetros adicionales,
"""
def a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return a_binario(n // 2) + str(n % 2)

print(a_binario(13))