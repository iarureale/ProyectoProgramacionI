"""
Implementar aplanar(datos) que transforme una lista de 
enteros que puede contener otras listas (con cualquier profundidad) en una sola lista plana, 
conservando el orden. Ejemplo: [1,[2,[3,4]],[],5] → [1,2,3,4,5]. No usar ciclos para recorrer los 
elementos. 
"""
def aplanar(datos):
    if not datos:
        return []
    elif isinstance(datos[0], list):
        return aplanar(datos[0]) + aplanar(datos[1:])
    else:
        return [datos[0]] + aplanar(datos[1:])

print(aplanar([1,[2,[3,4]],[],5]))