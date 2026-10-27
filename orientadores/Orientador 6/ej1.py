"""
Dada una lista de códigos de alumnos que puede contener repeticiones, desarrollen una función codigos_unicos(codigos) 
que retorne un conjunto con los códigos diferentes.
a) Informen cuántos códigos distintos hay. 
b) Verifiquen si el código 105 fue informado. 
c) Conviertan el conjunto en una lista ordenada para mostrar un resultado predecible. 
d) Expliquen qué información se pierde al convertir directamente una lista en conjunto. 
"""

codigos = [101, 103, 101, 105, 103, 108] 
unicos = set(codigos) 

def codigos_unicos(codigos):
    return set(codigos)

codigos_dif = codigos_unicos(codigos)
print(f"Hay {len(codigos_dif)} códigos distintos.")
for codigo in codigos_dif:
    print(codigo)

if 105 in codigos_dif:
    print("El código 105 fue informado.")
else:
    print("El código 105 NO fue informado")

print(sorted(codigos_dif))