"""
5. Máximo en lista no vacía. Implementar maximo_recursivo(datos) sin utilizar max() ni ciclos. 
Ejemplo: [4,9,1,7] → 9. Definir cómo tratar una lista vacía.
"""
def maximo_recursivo(datos):
    if datos == []:
        return 0
    if len(datos) == 1:
        return datos[0]

print(maximo_recursivo([4,9,1,7]))