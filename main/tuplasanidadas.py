#Ejercicio 7: Orientador 4
alumnos = (
 ("Ana", (12, "Marzo", 2005)),
 ("Bruno", (8, "Julio", 2004)),
 ("Carla", (21, "Enero", 2005))
)
print(alumnos[1][0])
print(alumnos[2][1])
print(alumnos[0][1][1])

for nombre, fecha in alumnos:
    dia, mes, año = fecha
    print(nombre, "-", dia, "de", mes, "de", año)

