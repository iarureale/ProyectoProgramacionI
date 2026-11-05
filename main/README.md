# OVERPALOOZA - Sistema de gestión del festival (Etapa 2)

Proyecto Integrador de **Programación I**. Programa de consola que gestiona la grilla de artistas (lineup) y la venta de entradas de un festival, con login de usuarios, persistencia en archivos y pruebas automatizadas.

Esta segunda etapa evoluciona el prototipo de la Etapa 1: se mantiene el mismo problema y las mismas reglas del festival, y se agregan configuración externa, persistencia, validaciones con expresiones regulares, manejo de excepciones y pruebas unitarias.

## Integrantes

- _Juan Cruz Isola_
- _Macarena Prieto_
- _Iara Reale_
- _Solana Cosenza_


## Requisitos

- Python 3.10 o superior
- `pytest` (solo para ejecutar las pruebas): `pip install pytest`

## Cómo ejecutar

Desde la carpeta del proyecto:

```
python main.py
```

Para ejecutar las pruebas unitarias:

```
pytest test_unitarias.py
```

Resultado esperado: `12 passed`.

## Estructura del proyecto

```
proyecto_etapa2/
├── main.py              # Punto de entrada: carga la configuración y arranca el menú
├── menu.py              # Interacción con el usuario (menús)
├── funciones.py         # Lógica del festival (grilla, artistas, disponibilidad, límites de compra)
├── validaciones.py      # Validaciones de formato con expresiones regulares
├── archivos.py          # Acceso a archivos (login, configuración, logs y compras)
├── configuracion.json   # Escenarios, horarios, precios y cupos
├── compras.csv          # Historial de compras
├── login.txt            # Cuentas de usuario (incluye las de administrador)
├── logs.json            # Intentos fallidos de inicio de sesión
├── test_unitarias.py    # Pruebas automatizadas (pytest)
└── README.md
```

## Funcionalidades

### Inicio
Menú con tres opciones: iniciar sesión, crear cuenta y salir. El rol de la cuenta (`Admin` o `Usuario`) determina qué menú se muestra.

### Usuario
- Consultar información general del festival
- Buscar artistas por código o nombre
- Consultar la grilla
- Comprar entradas (General y VIP)
- Ver estadísticas (sin información sensible)

### Administrador
- Consultar la grilla
- Registrar y modificar artistas (máximo 30)
- Ver estadísticas e informes, incluidos los intentos fallidos de inicio de sesión

### Estadísticas e informes
- **Ventas y recaudación** por categoría (General y VIP) y total acumulado
- **Ocupación y disponibilidad** por categoría y total
- **Lineup:** total y lista de artistas registrados
- **Intentos fallidos** por usuario (solo Admin), con alerta a partir de 3 intentos
- **Artistas por escenario**

### Alertas
- Al llegar a **3 intentos fallidos** de inicio de sesión se muestra una alerta, se bloquea el acceso y el programa termina.
- En el menú de compra se avisa cuando quedan **menos del 20%** de las entradas y cuando las entradas (en total o por categoría) se **agotaron**.

## Archivos y persistencia

| Archivo | Formato | Uso |
|---|---|---|
| `configuracion.json` | JSON | Escenarios, horarios, precio, cupo máximo y máximo por operación de cada tipo de entrada. **Obligatorio**: si falta o es inválido el programa informa el error y no inicia |
| `login.txt` | Texto (`;`) | Cuentas con `usuario;contraseña;mail;rol`. **Obligatorio**: contiene las cuentas Admin precargadas |
| `compras.csv` | CSV (`;`) | Una fila por compra: `id;fecha;nombre_completo;mail;dni;tipo_entrada;cantidad;monto_final`. Se crea automáticamente si no existe |
| `logs.json` | JSON | Lista de intentos fallidos con `user_ingresado`, `fecha` y `causa`. Se crea automáticamente si no existe. La contraseña ingresada nunca se guarda |

Las compras, las cuentas y los intentos fallidos se conservan entre ejecuciones. El archivo `compras.csv` se lee solo cuando se necesita (al comprar o consultar estadísticas) para que los datos reflejen siempre lo realmente registrado.

## Estructuras de datos

- **Diccionario acumulador de ventas:** `{"general": {"cantidad": n, "monto": m}, "vip": {...}}`, calculado recorriendo `compras.csv`.
- **Diccionario acumulador de intentos fallidos:** `{usuario: cantidad}`, construido a partir de `logs.json`.
- **Diccionario de configuración:** datos cargados desde `configuracion.json`.
- **Lineup:** matriz de 8 horarios x 5 escenarios, más dos listas paralelas (`codigos` y `nombre_artistas`). Se mantiene del modelo de la Etapa 1.

## Validaciones (expresiones regulares)

| Dato | Formato esperado |
|---|---|
| Usuario | 4 a 15 caracteres: letras, números o guion bajo |
| DNI | 7 u 8 dígitos, sin puntos |
| Mail | `nombre@dominio.ext` |

Además se valida el código de artista (`A-XX`), la cantidad de entradas (entero positivo, dentro del límite por operación y del stock) y la contraseña (mínimo 4 caracteres, al menos un número y sin `;`). Los mensajes de error indican qué formato se espera.

## Manejo de excepciones

Se controlan los archivos inexistentes (`FileNotFoundError`), los errores de lectura y escritura (`OSError`), las conversiones inválidas (`ValueError`) y la división por cero en el cálculo de disponibilidad (`ZeroDivisionError`). Las filas incorrectas de `compras.csv` se informan sin perder las válidas.

## Pruebas unitarias

`test_unitarias.py` contiene 12 pruebas para `pytest`. Ninguna usa `input` ni depende de mensajes en pantalla. Cubren validaciones correctas e incorrectas (incluida una excepción), un cálculo con resultado conocido, una acumulación por clave, la detección de condiciones críticas (stock agotado), casos límite y las expresiones regulares de usuario, mail y DNI.

## Alcance y decisiones

- El lineup (matriz y listas de artistas) vive en memoria y **no se guarda en archivos**: se reinicia en cada ejecución.
- Quedan **fuera de este alcance**: conjuntos (resumen de únicos), recursividad y persistencia del lineup.

## Cuentas de demostración

Cuenta de administrador precargada en `login.txt`: usuario `admin` (la contraseña está en ese mismo archivo). Las cuentas nuevas creadas desde el menú siempre tienen rol `Usuario`. `compras.csv` incluye datos de ejemplo para probar las estadísticas y las alertas de disponibilidad.
