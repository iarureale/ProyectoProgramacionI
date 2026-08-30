import funciones

equipo = []
roles = []
nombre_equipo = input('Ingresar nombre del equipo: ')
comision = input('Ingresar comisión: ')
funciones.ingresar_equipo(equipo, roles)
funciones.mostrar(equipo, roles, nombre_equipo,comision)
sigla = funciones.inicial(nombre_equipo)

print(f'Nuestro equipo {nombre_equipo} forma la sigla {sigla}')

funciones.verificacion(nombre_equipo)



