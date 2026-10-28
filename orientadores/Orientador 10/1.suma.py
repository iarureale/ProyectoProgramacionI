"""1. Suma de dígitos (inicial). Escribir suma_digitos(n) que reciba un entero natural y devuelva la 
suma de sus dígitos, sin convertirlo a cadena. Ejemplo: suma_digitos(5832) → 18. Contemplar n=0."""

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
        
print(suma_digitos(2342))