# 🎵 Overpalooza

Proyecto integrador desarrollado en **Python** para la materia **Programación I**.

## 📌 Descripción

**Overpalooza** es un sistema de gestión para un festival de música, con dos áreas que comparten el dominio del festival:

- **Programación del festival:** carga de artistas, asignación a escenarios y franjas horarias, y consulta de la grilla (lineup).
- **Venta de entradas:** comercialización de entradas General y VIP, control de disponibilidad, registro de compras y cálculo de indicadores económicos.

En la Etapa 2 se incorporan inicio de sesión con roles, validaciones con expresiones regulares, persistencia en archivos (CSV, JSON y TXT), diccionarios para el seguimiento de datos, manejo de excepciones, modularización del código y pruebas unitarias.

## 🆕 Novedades de la Etapa 2

- Expresiones regulares para validar usuario, DNI y email (además de código de artista, cantidad, id de compra y fecha).
- Diccionarios de registros (ventas), acumulador (intentos fallidos) y configuración.
- Conjuntos (`set`) para detectar valores repetidos de forma interna.
- Archivo `compras.csv`, creado automáticamente y actualizado con cada compra.
- Archivos JSON de configuración (`configuracion.json`) y de registro de ingresos fallidos (`logs.json`).
- Manejo de excepciones en la lectura y escritura de archivos, en las conversiones y en los cálculos.
- Login con dos roles (Admin y Usuario) a partir de `login.txt`, con creación de cuentas.
- Nuevos reportes: alertas, general y filtrado, todos consultables desde el menú de Estadísticas.
- Modularización del código en cinco módulos con responsabilidades separadas.
- Pruebas unitarias con pytest (12 pruebas automatizadas).

## Evolución respecto de la Etapa 1

En la Etapa 1 el programa guardaba todo en memoria: las constantes del festival estaban escritas en el código, las compras y los accesos se perdían al cerrar el programa y todas las funciones convivían en un solo archivo. En la Etapa 2 se mantuvieron las mismas reglas del festival y se resolvieron esas limitaciones:

- **Configuración en JSON:** escenarios, horarios, precios, cupos y máximo por operación pasaron a `configuracion.json`, para poder modificarlos sin tocar el código. Se valida su estructura al iniciar y, si el archivo falta o es inválido, el programa informa el error y no inicia, en lugar de reemplazarlo en silencio.
- **Persistencia con CSV:** las compras se guardan en `compras.csv`, una fila por operación. El archivo se lee al iniciar solo para informar las filas inválidas, y luego únicamente cuando se necesita (al comprar o al consultar estadísticas); no se mantiene en memoria, de modo que los datos siempre reflejan lo realmente registrado.
- **Usuarios y accesos:** login con `login.txt`, dos roles y creación de cuentas. Los intentos fallidos se registran en `logs.json` y se acumulan por usuario, lo que permite la alerta al tercer intento.
- **Validaciones con expresiones regulares:** funciones puras que devuelven `True` o `False`, separadas de la interacción con el usuario, para poder probarlas sin `input`.
- **Excepciones:** un error del usuario o de un archivo ya no termina el programa sin explicación.
- **Modularización:** se resolvió la dificultad de mantener y probar un único archivo extenso.

## 🔐 Login y roles

El menú inicial es:

```
1. Iniciar sesión
2. Crear cuenta
3. Salir
```

Las credenciales se guardan en `login.txt`, único archivo de usuarios del sistema, con el formato:

```
usuario;contraseña;mail;rol
```

El campo `rol` (`Admin` o `Usuario`) determina qué menú se muestra al iniciar sesión:

- **Usuario:** puede consultar información general del festival (submenú con Sponsors, Ingreso y apertura, Objetos no permitidos y Redes sociales), buscar artistas, consultar la grilla, comprar entradas y ver las estadísticas del festival. No accede a información sensible como los intentos fallidos de los usuarios: esa opción aparece en el menú de Estadísticas, pero muestra un aviso de falta de privilegios.
- **Admin:** puede consultar la grilla, registrar y modificar artistas en el lineup (ambos desde "Modificar programación") y ver todas las estadísticas e informes del sistema, incluidos los intentos fallidos.

### Inicio de sesión

Solo se solicitan usuario y contraseña. El mail no se pide en este paso. **Únicamente se valida el formato del usuario**; la contraseña se compara tal cual contra `login.txt`.

### Creación de cuentas

Las cuentas de administrador vienen cargadas previamente en el archivo; las cuentas de usuario se crean desde el menú principal. Al crear una cuenta es obligatorio ingresar:

- **Usuario:** con el formato válido y no puede estar repetido (sin distinguir mayúsculas).
- **Mail:** obligatorio, con formato válido (`nombre@dominio.ext`) y no puede estar repetido (sin distinguir mayúsculas).
- **Contraseña:** al menos 4 caracteres, incluir al menos un número y no puede contener el carácter `;` (separador del archivo).

Las cuentas creadas siempre se registran con el rol `Usuario`. Las contraseñas se guardan en texto plano en `login.txt`; esto se acepta como limitación del alcance del proyecto.

### Intentos fallidos de ingreso

- Cada intento fallido se registra en `logs.json` con el usuario ingresado, la fecha (`dd-mm-aaaa`) y la causa del fallo: `"Usuario no encontrado."`, `"Usuario con formato incorrecto."` o `"Los campos no coinciden."`.
- Nunca se guarda la contraseña ingresada.
- Si `logs.json` no existe, se crea automáticamente al registrar el primer intento fallido.
- Los intentos se cuentan por cada vez que se ingresan credenciales incorrectas durante la ejecución del programa, y el contador se reinicia con un login exitoso.
- Al llegar a **3 intentos fallidos** se genera una alerta (mensaje en pantalla), se bloquea el acceso y el programa se termina.

Protecciones de `logs.json`: si no existe se considera vacío; los elementos con estructura incorrecta se ignoran; y si el archivo está dañado no se sobrescribe, para no perder el historial (el intento no se registra y se informa el error).

Ejemplo de `logs.json`:

```json
[
  {
    "user_ingresado": "Juan_234",
    "fecha": "21-10-2026",
    "causa": "Los campos no coinciden."
  }
]
```

## ✅ Validaciones (expresiones regulares)

Cada formato tiene un mensaje de error que indica qué se espera:

| Dato | Formato esperado | Dónde se usa |
|---|---|---|
| Usuario | 4 a 15 caracteres: letras, números o guion bajo | Login / Crear cuenta |
| DNI | 7 u 8 dígitos, solo números y sin puntos | Compra de entradas |
| Email | Estructura `nombre@dominio.ext` | Crear cuenta / Compra de entradas |

También se validan con expresiones regulares el código de artista (`A-XX`), la cantidad de entradas (entero positivo), el id de compra (4 dígitos, entre 1000 y 9999) y la fecha (`dd-mm-aaaa`, que además debe existir en el calendario). La contraseña se valida **sin** expresión regular.

Las validaciones son funciones puras (`es_usuario_valido`, `es_dni_valido`, `es_mail_valido`, `es_contrasena_valida`, `es_fecha_valida`, `validar_fila_compra` y `validar_configuracion`) que devuelven `True` o `False` (o, en las dos últimas, el resultado de la validación sin pedir datos por teclado). La interacción con el usuario está en funciones aparte.

## 🗂️ Estructuras de datos

### Diccionarios

**Diccionario de registros (ventas por tipo de entrada):** acumula las ventas con una clave por cada tipo (`general` y `vip`); cada una guarda la cantidad de entradas vendidas y el monto total recaudado.

```python
{
    "general": {"cantidad": 3, "monto": 300000.0},
    "vip":     {"cantidad": 2, "monto": 500000.0}
}
```

La función `calcular_total()` parte del diccionario en cero y recorre `compras.csv` fila por fila, sumando `cantidad` y `monto_final` en la clave que corresponda a `tipo_entrada`. Retorna la tupla `(total_entradas, monto_total, total_general, total_vip)`. Así las ventas siempre se calculan a partir de lo realmente registrado en el archivo.

**Diccionario acumulador (intentos fallidos por usuario):** `crear_reporte()` lee `logs.json`, recorre la lista y arma un diccionario donde la clave es el usuario y el valor, la cantidad de intentos fallidos. Por ejemplo, tres intentos de `admin` y uno de `juan` generan `{"admin": 3, "juan": 1}`. Si el usuario todavía no figura, parte de 0.

**Diccionario de configuración:** carga desde `configuracion.json` las variables fijas (escenarios, horarios, precios, cupos y máximo por operación). Al iniciar se valida su estructura (`validar_configuracion`):

- Exactamente 5 escenarios y 8 horarios, textos no vacíos y sin repetidos.
- Entradas General y VIP, cada una con `precio`, `cupo_maximo` y `max_operacion` numéricos y positivos.
- `cupo_maximo` y `max_operacion` enteros, y `max_operacion` no mayor que `cupo_maximo`.

La cantidad de escenarios (5) y de horarios (8) está fija por el tamaño de la grilla.

### Conjuntos

Los conjuntos (`set`) se usan de forma interna, siempre para detectar valores repetidos:

- En `calcular_total()`, el conjunto `ids_vistos` guarda el id de cada compra válida; si el id de una fila ya está en el conjunto, esa fila se descarta por "id repetido" y no se suma a los totales.
- En `validar_configuracion()`, un conjunto por comprensión con los escenarios (y otro con los horarios), sin espacios extra y sin distinguir mayúsculas, se compara en tamaño con la lista original: si son distintos, hay valores repetidos y el archivo se rechaza.

Los conjuntos no se usan para generar un reporte de valores únicos.

### Archivos

**`configuracion.json`**

```json
{
  "escenarios": ["McStage", "PStage", "FIATStage", "FlowStage", "SanStage"],
  "horarios": ["13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"],
  "entradas": {
    "General": { "precio": 100000, "cupo_maximo": 80, "max_operacion": 6 },
    "VIP":     { "precio": 250000, "cupo_maximo": 20, "max_operacion": 6 }
  }
}
```

Los precios, cupos y nombres se pueden modificar sin tocar el código.

**`compras.csv`** se crea automáticamente (con su encabezado) al registrar la primera compra, si no existe o está vacío, y se actualiza con cada compra (una fila nueva por operación, campos separados por `;`):

```
id;fecha;nombre_completo;mail;dni;tipo_entrada;cantidad;monto_final
```

| Campo | Descripción |
|---|---|
| `id` | Número de 4 dígitos (1000–9999), generado automáticamente y sin repetirse en el archivo. |
| `fecha` | Día de la compra (formato `dd-mm-aaaa`). |
| `nombre_completo` | Nombre del responsable de la entrada; no puede estar vacío ni contener `;`. |
| `mail` | Correo del comprador, validado con el formato `nombre@dominio.ext`. |
| `dni` | Documento del comprador (7 u 8 dígitos). |
| `tipo_entrada` | `general` o `vip`. |
| `cantidad` | Entradas de la operación (entero positivo, hasta el menor valor entre `max_operacion` y el stock restante). |
| `monto_final` | Total abonado (cantidad por el precio de la categoría). |

El nombre, el mail y el DNI se solicitan en cada compra, ya que pueden ser distintos a los de la cuenta con la que se inició sesión.

**Filas descartadas.** Al recorrer el archivo, `calcular_total()` descarta una fila (sin perder las demás) si:

- no tiene 8 columnas;
- el id no tiene 4 dígitos o está repetido;
- la fecha, el nombre, el DNI o el mail son inválidos;
- el tipo de entrada no es `general` ni `vip`;
- la cantidad no es un entero positivo o supera el máximo por operación;
- el monto no coincide con cantidad × precio configurado;
- sumar la fila superaría el cupo máximo de ese tipo de entrada.

Si la primera línea no es el encabezado esperado, se informa y se procesa el archivo desde esa línea. Los avisos de filas descartadas se muestran **una sola vez, al iniciar el programa** (`main.py` llama a `calcular_total` con `mostrar_avisos=True`); las consultas posteriores (compra y estadísticas) calculan los totales sin repetir los avisos.

**`logs.json`** registra los intentos de inicio de sesión fallidos (ver *Intentos fallidos de ingreso*).

## 🎤 Programación del festival (lineup)

Se mantiene el modelo de datos de la Etapa 1:

- Hasta **30 artistas**, identificados por un código único con formato `A-` + dos dígitos (ej: `A-01`). Al alcanzar el límite, el sistema informa que no se admiten más registros.
- 5 escenarios y 8 franjas horarias (13:00 a 20:00).
- **Lineup:** matriz bidimensional de 8 filas × 5 columnas. Las filas son las franjas horarias y las columnas, los escenarios. La función `grilla()` de `funciones.py` la crea con `'.'` en cada celda y `main.py` la inicializa al arrancar. Cada celda guarda el código del artista asignado (`A-XX`) o `'.'` si está libre.
- **Artistas:** dos listas paralelas, `codigos` (formato `A-XX`, únicos) y `nombre_artistas` (nombres únicos, sin distinguir mayúsculas ni espacios extra), en correspondencia por índice.
- **Asignación:** una combinación horario/escenario ocupada no se puede asignar y se vuelve a pedir.
- **Modificación:** se puede cambiar el código, el nombre, el horario (dentro del mismo escenario) o el escenario (dentro del mismo horario) de un artista ya registrado.
- **Consulta:** la grilla se muestra por código y por nombre. La búsqueda de artistas acepta código o nombre.
- **Conteo:** la cantidad total de artistas se calcula contando los elementos de `codigos`, y la cantidad por escenario recorriendo las celdas de la matriz que difieren de `'.'`.
- Registrar y modificar artistas es una función exclusiva del rol **Admin**; consultar la grilla está disponible para ambos roles y buscar artistas, para el rol Usuario.

> ⚠️ **Persistencia:** la grilla y las listas `codigos` y `nombre_artistas` viven solo en memoria durante la ejecución y se reinician cada vez que se corre el programa. Guardarlas en archivos queda fuera del alcance de la Etapa 2.

## 🎫 Entradas

| Tipo | Precio | Cupo máximo | Máx. por operación |
|---|---|---|---|
| General | $100.000 | 80 | 6 |
| VIP | $250.000 | 20 | 6 |

- Capacidad total del festival: 100 entradas (80 General + 20 VIP), calculada como la suma de los cupos de la configuración.
- El menú de compra tiene tres opciones: comprar entradas (tipo, cantidad y confirmación), chequear disponibilidad total y salir.
- El límite de compra por operación es dinámico: es el menor entre el máximo por operación (6) y el stock restante de esa categoría (devuelve 0 si el stock es cero).
- La cantidad debe ser un número entero positivo. El nombre, el mail y el DNI se piden en cada compra y se validan con el formato correspondiente antes de guardarla.
- Cada compra registra nombre completo, mail, DNI, tipo de entrada, cantidad y monto final en `compras.csv`. No se almacenan datos de pago.
- Las alertas de disponibilidad se evalúan y se muestran cada vez que se ingresa al menú de compra:
  - entradas agotadas en total (disponibilidad igual o menor a 0%);
  - menos del 20% de entradas disponibles sobre el total;
  - categoría General o VIP agotada, cuando todavía quedan entradas de la otra.

## 🔎 Búsquedas y ordenamientos

- Búsqueda de artista por código o por nombre, mostrando nombre, escenario y horario asignado.
- Listado de artistas ordenado alfabéticamente (`sorted()`).
- Uso de listas por comprensión para construir la matriz de `lineup`.

## 📊 Reportes

Los reportes general y filtrado se muestran en consola, desde el menú de Estadísticas (opciones 1 a 5).

### Reporte de alertas

Lleva la cuenta de los intentos de inicio de sesión fallidos de la ejecución. Al llegar a 3 intentos se emite un mensaje de alerta en pantalla, se bloquea el acceso y el programa se termina. Todos los intentos quedan registrados en `logs.json`.

### Reporte general

Informe del festival que incluye:

**Ventas y recaudación**

- Cantidad total de entradas General vendidas y su recaudación parcial ($).
- Cantidad total de entradas VIP vendidas y su recaudación parcial ($).
- Total de entradas vendidas y recaudación total acumulada del festival ($).

**Ocupación y disponibilidad**

- Porcentaje total de ocupación (entradas vendidas sobre la capacidad global, que es la suma de los cupos de la configuración: 100 entradas con la configuración actual).
- Porcentaje de ocupación de cada categoría.
- Las alertas de entradas agotadas y de menos del 20% disponible se muestran en el menú de compra.

**Programación (lineup)**

- Total de artistas registrados en el sistema (`len(codigos)`).
- Lista de todos los artistas registrados, en orden de carga.
- Cantidad de artistas asignados a cada escenario.

**Accesos y alertas** (solo Admin)

- Total acumulado de intentos fallidos de inicio de sesión registrados en el sistema, con el detalle de intentos por usuario y la marca `[ALERTA: 3 o más intentos]` para quienes llegan a 3.

### Reporte filtrado

Corresponde a las opciones "Ventas y recaudación" y "Ocupación y disponibilidad" del menú de Estadísticas. Muestra los datos separados por categoría (General y VIP):

- La cantidad vendida se calcula desde `compras.csv`, por lo que incluye las compras de la sesión actual y de ejecuciones anteriores.
- La recaudación de cada categoría es la cantidad vendida por el precio configurado.
- La recaudación total acumulada se suma desde la columna `monto_final`. Ambos valores coinciden porque las filas con monto distinto de cantidad × precio se descartan.

## ⚠️ Manejo de excepciones

Se usan excepciones para que un error del usuario o de un archivo no finalice el programa sin intención y para informar por qué falló:

- **`FileNotFoundError`:** `compras.csv` y `logs.json` se crean automáticamente si no existen. `configuracion.json` y `login.txt` no se reemplazan en silencio si faltan: se informa el error y el programa no inicia. Además, `login.txt` debe tener al menos una cuenta Admin válida.
- **Filas CSV con formato incorrecto:** se informan al iniciar, sin perder las filas válidas.
- **`OSError`** en lectura y escritura de archivos y **`ValueError`** en conversiones y en la lectura de JSON.
- **`RecursionError`:** JSON con anidación excesiva.
- **`ZeroDivisionError`:** en el cálculo de disponibilidad, si un cupo configurado fuera 0. Los menús de compra y estadísticas muestran un mensaje de error de configuración en lugar de cerrarse.

## 🧪 Pruebas unitarias

El archivo `test_unitarias.py` incluye 12 pruebas automatizadas escritas para pytest. Ninguna solicita datos mediante `input` ni depende de mensajes mostrados por pantalla: todas verifican únicamente los valores que devuelven las funciones.

Para ejecutarlas:

```
pytest test_unitarias.py
```

Casos cubiertos:

- **Validación correcta:** un código de artista válido (`A-01`) y una cantidad de entradas válida (`1`) son aceptados.
- **Validación incorrecta:** códigos con formato inválido (`B-01`, `A-1`) y una cantidad inválida (`0`) son rechazados. Además, calcular la disponibilidad con capacidad igual a cero produce `ZeroDivisionError`.
- **Cálculo simple con resultado conocido:** la disponibilidad con 5 entradas vendidas sobre una capacidad de 10 es del 50%.
- **Acumulación por clave:** el conteo de artistas por escenario recorre la matriz `lineup`. Con tres artistas cargados, el resultado esperado es `[2, 0, 1, 0, 0]`.
- **Detección de condición crítica:** el límite de compra devuelve 0 cuando el stock restante de entradas General o VIP es cero.
- **Casos límite:** cantidad 0, stock restante exactamente en cero, capacidad igual a cero y DNI de 7 dígitos (válido) frente a uno de 6 (inválido).
- **Expresiones regulares:** usuario, mail y DNI válidos son aceptados; inválidos (por ejemplo `a`, `nombre@gmail` y un DNI de 6 dígitos) son rechazados, incluyendo el límite inferior de 7 dígitos del DNI.

## 🏗️ Arquitectura

```
proyecto_etapa2/
│
├── main.py             # Punto de entrada; carga la configuración, verifica archivos obligatorios e inicializa lineup y listas
├── menu.py             # Menús y flujo de navegación del usuario
├── funciones.py        # Lógica del festival (grilla, artistas, disponibilidad, límites de compra) y funciones de ingreso por teclado
├── validaciones.py     # Validaciones de formato con regex (funciones puras, sin input)
├── archivos.py         # Acceso a archivos: login.txt, configuracion.json, logs.json y compras.csv
├── test_unitarias.py   # 12 pruebas automatizadas con pytest
├── logs.json           # Intentos de ingreso fallidos
├── configuracion.json  # Escenarios, horarios y entradas
├── compras.csv         # Compras realizadas
├── login.txt           # Usuarios y roles
└── README.md
```

### Organización del código

- `main.py` inicia el programa: carga y valida la configuración, verifica que `login.txt` se pueda leer y tenga al menos una cuenta Admin, informa las filas inválidas de `compras.csv`, crea el lineup vacío y las listas de artistas, y lanza el menú principal.
- `menu.py` contiene los menús y el flujo de navegación del usuario, incluidos los pedidos de datos propios de cada menú (por ejemplo, la cantidad de entradas).
- `funciones.py` contiene la lógica del festival y las funciones que piden datos por teclado y repiten la consulta hasta que sean válidos (por ejemplo, el mail, el DNI o la contraseña).
- `validaciones.py` agrupa las validaciones de formato con expresiones regulares y de datos ingresados; son funciones puras, por lo que pueden probarse automáticamente con pytest.
- `archivos.py` concentra el acceso a los archivos y no pide datos por teclado: recibe los datos ya validados y se limita a leerlos o escribirlos.

`funciones.py` importa los otros dos módulos, de modo que `menu.py` y las pruebas acceden a todas las funciones desde un único punto.

## 🚫 Fuera de este alcance

- Recursividad.
- Persistencia en archivos de la matriz de lineup y de las listas `codigos` y `nombre_artistas`.
- Cifrado de contraseñas.
- "Resumen de Únicos": los conjuntos se usan solo de forma interna, para detectar valores repetidos.
- Pagos reales, almacenamiento de tarjetas, entradas digitales/QR, devoluciones, envío de mails, aplicación web, control de ingreso al predio y múltiples días de festival.

## ▶️ Ejecución

Clonar el repositorio:

```
git clone https://github.com/iarureale/ProyectoProgramacionI.git
```

Luego ejecutar `main.py` con Python desde la carpeta que lo contiene (`main/`):

```
cd main
python main.py
```

Para correr las pruebas unitarias (requiere pytest):

```
pip install pytest
pytest test_unitarias.py
```

## 👥 Integrantes

**Programación I**

- Iara Reale
- Macarena Prieto
- Solana Cosenza
- Juan Cruz Isola
