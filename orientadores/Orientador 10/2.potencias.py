"""
2. Potencia por multiplicaciones. Implementar potencia(base, exponente) con exponente entero 
no negativo, sin usar ** ni pow(). Ejemplo: potencia(3,4) → 81. Explicar qué ocurre con el exponente 
cero. 
"""
def potencia(base, exponente):
    if exponente < 0:
        return -0
    elif exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente -1)

print(potencia(4, 5))