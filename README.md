# 🎵 Overpalooza

Proyecto integrador desarrollado en **Python** para la materia **Algoritmos y Estructuras de Datos I**.

## 📌 Descripción

**Overpalooza** es un sistema de gestión para un festival de música, con dos áreas que comparten el dominio del festival:

* **Programación del festival:** carga de artistas, asignación a escenarios y franjas horarias, y consulta de la grilla (lineup).
* **Venta de entradas:** comercialización de entradas General y VIP, control de disponibilidad, registro de compras y cálculo de indicadores económicos.

En la **Etapa 2** se incorporan inicio de sesión con roles, validaciones con expresiones regulares, persistencia en archivos (CSV, JSON y TXT), diccionarios para el seguimiento de datos, manejo de excepciones, modularización del código y pruebas unitarias.

## 🆕 Novedades de la Etapa 2

1. **Expresiones regulares** para validar usuario, DNI y email.
2. **Diccionarios** de registros, acumulador y configuración.
3. **Archivo `compras.csv`**, creado automáticamente y actualizado con cada compra.
4. **Archivos JSON** de configuración (`configuracion.json`) y de registro de ingresos fallidos (`logs.json`).
5. **Manejo de excepciones** en todo el programa.
6. **Login con dos roles** (Admin y Usuario) a partir de `login.txt`, con creación de cuentas.
7. **Nuevos reportes:** alertas, general y filtrado, todos consultables desde el menú de Estadísticas.
8. **Modularización** del código en cinco módulos con responsabilidades separadas.
9. **Pruebas unitarias** con pytest (12 pruebas automatizadas).

### Evolución respecto de la Etapa 1

En la Etapa 1 el programa guardaba todo en memoria: las constantes del festival estaban escritas en el código, las compras y los accesos se perdían al cerrar el programa y todas las funciones convivían en un solo archivo. En la Etapa 2 se mantuvieron las mismas reglas del festival y se resolvieron esas limitaciones:

* **Configuración en JSON:** escenarios, horarios, precios, cupos y máximo por operación pasaron a `configuracion.json`, para poder modificarlos sin tocar el código. Si el archivo falta o es inválido, el programa informa el error y no inicia, en lugar de reemplazarlo en silencio.
* **Persistencia con CSV:** las compras se guardan en `compras.csv`, una fila por operación. El archivo se lee solo cuando se necesita (al comprar o al consultar estadísticas) y no se carga en memoria al iniciar, de modo que los datos siempre reflejan lo realmente registrado.
* **Usuarios y accesos:** login con `login.txt` y dos roles. Los intentos fallidos se registran en `logs.json`.
* **Validaciones con expresiones regulares:** funciones puras que devuelven `True` o `False`, separadas de la interacción con el usuario, para poder probarlas sin `input`.
* **Excepciones:** un error del usuario ya no termina el programa sin explicación.
* **Modularización:** se resolvió la dificultad de mantener y probar un único archivo extenso.

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

* **Usuario:** puede consultar información general del festival, buscar artistas, consultar la grilla, comprar entradas y ver las estadísticas del festival, pero **no** información sensible como los intentos fallidos de los usuarios.
* **Admin:** puede consultar la grilla, registrar y modificar artistas en el lineup, y ver las estadísticas e informes del sistema (incluidos los intentos fallidos).

### Inicio de sesión

Solo se solicitan **usuario y contraseña**. El mail no se pide en este paso.

### Creación de cuentas

Las cuentas de administrador vienen cargadas previamente en el archivo; las cuentas de usuario se crean desde el menú principal. Al crear una cuenta es obligatorio ingresar:

* **Usuario:** con el formato válido y no puede estar repetido.
* **Mail:** obligatorio, con formato válido (`nombre@dominio.ext`) y no puede estar repetido.
* **Contraseña:** al menos 4 caracteres, incluir al menos un número y no puede contener el carácter `;` (separador del archivo).

Las cuentas creadas siempre se registran con el rol **Usuario**.

### Intentos fallidos de ingreso

* Cada intento fallido se registra en `logs.json` con el **usuario ingresado**, la **fecha** (`dd-mm-aaaa`) y la **causa** del fallo: `"Usuario no encontrado."`, `"Usuario con formato incorrecto."` o `"Los campos no coinciden."`.
* **Nunca se guarda la contraseña ingresada.**
* Si `logs.json` no existe, se crea automáticamente al registrar el primer intento fallido.
* Los intentos se cuentan por cada vez que se ingresan credenciales incorrectas durante la ejecución del programa, y el contador **se reinicia con un login exitoso**.
* Al llegar a **3 intentos fallidos** se genera una alerta (mensaje en pantalla), se bloquea el acceso y **el programa se termina**.

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

| Dato    | Formato esperado                                | Dónde se usa                         |
|---------|-------------------------------------------------|--------------------------------------|
| Usuario | 4 a 15 caracteres: letras, números o guión bajo | Login / Crear cuenta                 |
| DNI     | 7 u 8 dígitos                                   | Compra de entradas                   |
| Email   | Estructura `nombre@dominio.ext`                 | Crear cuenta / Compra de entradas    |

Las validaciones son funciones puras (`es_usuario_valido`, `es_dni_valido`, `es_mail_valido`, `es_contrasena_valida`) que devuelven `True` o `False`.

## 🗂️ Estructuras de datos

### Diccionarios

* **Diccionario de registros (ventas por tipo de entrada):** acumula las ventas con una clave por cada tipo (`general` y `vip`); cada una guarda la cantidad de entradas vendidas y el monto total recaudado.

  ```python
  {
      "general": {"cantidad": 3, "monto": 300000.0},
      "vip":     {"cantidad": 2, "monto": 500000.0}
  }
  ```

  La función `calcular_total()` parte del diccionario en cero y recorre `compras.csv` fila por fila, sumando `cantidad` y `monto_final` en la clave que corresponda a `tipo_entrada`. Así las ventas siempre se calculan a partir de lo realmente registrado en el archivo.

* **Diccionario acumulador (intentos fallidos por usuario):** el sistema lee `logs.json`, recorre la lista y arma un diccionario donde la clave es el usuario y el valor, la cantidad de intentos fallidos. Por ejemplo, tres intentos de `admin` y uno de `juan` generan `{"admin": 3, "juan": 1}`. Si el usuario todavía no figura, parte de 0.

* **Diccionario de configuración:** carga desde `configuracion.json` las variables fijas (escenarios, horarios, precios, cupos y máximo por operación).

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

**`compras.csv`** se crea automáticamente si no existe y se actualiza con cada compra (una fila nueva por operación, campos separados por `;`):

```
id;fecha;nombre_completo;mail;dni;tipo_entrada;cantidad;monto_final
```

| Campo             | Descripción                                                          |
|-------------------|----------------------------------------------------------------------|
| `id`              | Número único de 4 dígitos, generado automáticamente.                 |
| `fecha`           | Día de la compra (formato `dd-mm-aaaa`).                             |
| `nombre_completo` | Nombre del responsable de la entrada.                                |
| `mail`            | Correo del comprador, validado con el formato `nombre@dominio.ext`.  |
| `dni`             | Documento del comprador (7 u 8 dígitos).                             |
| `tipo_entrada`    | `general` o `vip`.                                                   |
| `cantidad`        | Cantidad de entradas compradas en la operación.                      |
| `monto_final`     | Total abonado (cantidad por el precio de la categoría).              |

El mail se solicita nuevamente en cada compra, ya que puede ser distinto al de la cuenta con la que se inició sesión.

**`logs.json`** registra los intentos de inicio de sesión fallidos (ver [Intentos fallidos de ingreso](#intentos-fallidos-de-ingreso)).

## 🎤 Programación del festival (lineup)

Se mantiene el modelo de datos de la Etapa 1:

* Hasta **30 artistas**, identificados por un código único con formato `A-` + dos dígitos (ej: `A-01`). Al alcanzar el límite, el sistema informa que no se admiten más registros.
* 5 escenarios y 8 franjas horarias (13:00 a 20:00).
* **Lineup:** matriz bidimensional de 8 filas × 5 columnas. Las filas son las franjas horarias y las columnas, los escenarios. La función `grilla()` de `funciones.py` la crea con `'.'` en cada celda y `main.py` la inicializa al arrancar. Cada celda guarda el código del artista asignado (`A-XX`) o `'.'` si está libre.
* **Artistas:** dos listas paralelas, `codigos` (claves únicas) y `nombre_artistas` (nombres artísticos, en correspondencia por índice).
* **Conteo:** la cantidad total de artistas se calcula contando los elementos de `codigos`, y la cantidad por escenario recorriendo las celdas de la matriz que difieren de `'.'`.
* Antes de asignar o modificar un artista se valida, en orden: que el código exista y no esté repetido, que el escenario exista, que el horario sea válido, que el artista no esté ya programado en otro lugar y que la combinación escenario/horario esté libre.
* Registrar y modificar artistas es una función exclusiva del rol **Admin**; consultar la grilla y buscar artistas está disponible para ambos roles.

> ⚠️ **Persistencia:** la grilla y las listas `codigos` y `nombre_artistas` viven solo en memoria durante la ejecución y se reinician cada vez que se corre el programa. Guardarlas en archivos queda fuera del alcance de la Etapa 2.

## 🎫 Entradas

| Tipo    | Precio    | Cupo máximo | Máx. por operación |
|---------|-----------|-------------|--------------------|
| General | $100.000  | 80          | 6                  |
| VIP     | $250.000  | 20          | 6                  |

* Capacidad total del festival: 100 entradas (80 General + 20 VIP).
* El límite de compra por operación es dinámico: es el menor entre 6 y el stock restante de esa categoría (devuelve 0 si el stock es cero).
* Antes de confirmar una compra se valida disponibilidad, que la cantidad sea un número entero positivo y que el DNI y el mail tengan formato válido.
* Cada compra registra nombre completo, mail, DNI, tipo de entrada, cantidad y monto final en `compras.csv`. No se almacenan datos de pago.
* Las alertas de **entradas agotadas** (en total y por categoría) y de **menos del 20% de entradas disponibles** (sobre el total) se muestran en el menú de compra de entradas cada vez que se accede a él.

## 🔎 Búsquedas, ordenamientos y rankings

* Búsqueda de artista por código o por nombre, mostrando nombre, escenario y horario asignado.
* Listado de artistas ordenado alfabéticamente (`sorted()`).
* Encuesta al momento de comprar: el usuario vota cuál escenario tiene el mejor lineup (1 al 5). El ranking se arma con una lista paralela a escenarios y se ordena con `.sort()` y `lambda`.
* Uso de listas por comprensión para construir la matriz de `lineup`.

## 📊 Reportes

Los reportes general y filtrado se muestran **en consola, desde el menú de Estadísticas**.

### Reporte de alertas

Lleva la cuenta de los intentos de inicio de sesión fallidos. Al llegar a 3 intentos se emite un mensaje de alerta en pantalla, se bloquea el acceso y el programa se termina. Todos los intentos quedan registrados en `logs.json`.

### Reporte general

Informe del festival que incluye:

**Ventas y recaudación**

* Cantidad total de entradas General vendidas y su recaudación parcial ($).
* Cantidad total de entradas VIP vendidas y su recaudación parcial ($).
* Recaudación total acumulada del festival ($).
* Porcentaje total de ocupación (entradas vendidas sobre la capacidad global de 100 entradas).
* Estado de disponibilidad: las alertas de entradas agotadas y de menos del 20% disponible se muestran en el menú de compra; el porcentaje de ocupación por categoría se consulta en Estadísticas.

**Programación (lineup)**

* Total de artistas registrados en el sistema.
* Lista de todos los artistas registrados.
* Cantidad de artistas asignados a cada escenario.

**Accesos y alertas**

* Total acumulado de intentos fallidos de inicio de sesión registrados en el sistema, con el detalle de intentos por usuario. **Esta información solo está disponible para el Admin.**

### Reporte filtrado

Corresponde a las opciones **"Ventas y recaudación"** y **"Ocupación y disponibilidad"** del menú de Estadísticas. Muestra los datos separados por categoría (**General** y **VIP**):

* La cantidad vendida se calcula desde `compras.csv`, por lo que incluye las compras de la sesión actual y de ejecuciones anteriores.
* La recaudación de cada categoría es la cantidad vendida por el precio configurado.
* Los avisos de disponibilidad se muestran en el menú de compra de entradas.

## ⚠️ Manejo de excepciones

Se usan excepciones para que un error del usuario no finalice el programa sin intención y para informar por qué falló:

* **`FileNotFoundError`:** `compras.csv` y `logs.json` se crean automáticamente si no existen. `configuracion.json` y `login.txt` **no** se reemplazan en silencio si faltan: se informa el error.
* **Filas CSV con formato incorrecto:** se informan sin perder las filas válidas.
* **`OSError`** en lectura/escritura de archivos y **`ValueError`** en conversiones.

## 🧪 Pruebas unitarias

El archivo `test_unitarias.py` incluye **12 pruebas automatizadas** escritas para [pytest](https://docs.pytest.org/). Ninguna solicita datos mediante `input` ni depende de mensajes mostrados por pantalla: todas verifican únicamente los valores que devuelven las funciones.

Para ejecutarlas:

```bash
pytest test_unitarias.py
```

Casos cubiertos:

* **Validación correcta:** un código de artista válido (`A-01`) y una cantidad de entradas válida (`1`) son aceptados.
* **Validación incorrecta:** códigos con formato inválido (`B-01`, `A-1`) y una cantidad inválida (`0`) son rechazados. Además, calcular la disponibilidad con capacidad igual a cero produce `ZeroDivisionError`.
* **Cálculo simple con resultado conocido:** la disponibilidad con 5 entradas vendidas sobre una capacidad de 10 es del 50%.
* **Acumulación por clave:** el conteo de artistas por escenario recorre la matriz `lineup`. Con tres artistas cargados, el resultado esperado es `[2, 0, 1, 0, 0]`.
* **Detección de condición crítica:** el límite de compra devuelve 0 cuando el stock restante de entradas General o VIP es cero.
* **Caso límite:** cantidad 0, stock restante exactamente en cero y capacidad igual a cero.
* **Expresiones regulares:** usuario, mail y DNI válidos son aceptados; inválidos (por ejemplo `a`, `nombre@gmail` y un DNI de 6 dígitos) son rechazados, incluyendo el límite inferior de 7 dígitos del DNI.

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

* **`main.py`** inicia el programa: carga la configuración, verifica que existan los archivos obligatorios (`configuracion.json` y `login.txt`) y lanza el menú principal.
* **`menu.py`** contiene los menús y el flujo de navegación del usuario.
* **`funciones.py`** contiene la lógica del festival y las funciones que piden datos por teclado y repiten la consulta hasta que sean válidos (por ejemplo, el mail, el DNI o la contraseña).
* **`validaciones.py`** agrupa las validaciones de formato con expresiones regulares y de datos ingresados; son funciones puras que reciben un valor y devuelven `True` o `False`, por lo que pueden probarse automáticamente con pytest.
* **`archivos.py`** concentra el acceso a los archivos y no pide datos por teclado: recibe los datos ya validados y se limita a leerlos o escribirlos.

`funciones.py` importa los otros dos módulos, de modo que `menu.py` y las pruebas acceden a todas las funciones desde un único punto.

## 🚫 Fuera de este alcance

* Conjuntos y resumen de únicos.
* Recursividad.
* Persistencia en archivos de la matriz de lineup y de las listas `codigos` y `nombre_artistas`.
* Pagos reales, almacenamiento de tarjetas, entradas digitales/QR, devoluciones, envío de mails, aplicación web, control de ingreso al predio y múltiples días de festival.

## ▶️ Ejecución

Clonar el repositorio:

```bash
git clone https://github.com/iarureale/ProyectoProgramacionI.git
```

Luego ejecutar `main.py` con Python desde la carpeta del proyecto:

```bash
python main.py
```

Para correr las pruebas unitarias (requiere `pytest`):

```bash
pip install pytest
pytest test_unitarias.py
```

## 👥 Integrantes

**Algoritmos y Estructuras de Datos I**

* Iara Reale
* Macarena Prieto
* Solana Cosenza
* Juan Cruz Isola
