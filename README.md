# 🎵 Overpalooza

Proyecto integrador desarrollado en **Python** para la materia **Algoritmos y Estructuras de Datos I**.

## 📌 Descripción

**Overpalooza** es un sistema de gestión para un festival de música, con dos áreas que comparten el dominio del festival:

* **Programación del festival:** carga de artistas, asignación a escenarios y franjas horarias, y consulta de la grilla (lineup).
* **Venta de entradas:** comercialización de entradas General y VIP, control de disponibilidad, registro de compras y cálculo de indicadores económicos.

En la **Etapa 2** se incorporan inicio de sesión con roles, validaciones con expresiones regulares, persistencia en archivos (CSV, JSON y TXT), diccionarios para el seguimiento de datos y manejo de excepciones.

## 🆕 Novedades de la Etapa 2

1. Expresiones regulares para validar usuario, DNI y email.
2. Diccionarios de registros, de acumulador y de configuración.
3. Archivo `compras.csv` actualizado con cada compra.
4. Archivos JSON de configuración y de registro de ingresos fallidos.
5. Manejo de excepciones en todo el programa.
6. Login con dos roles (Admin y Usuario) desde `login.txt`.
7. Nuevos reportes: alertas, general (`informe.txt`) y filtrado por tipo de entrada (leído desde `compras.csv`).

## 🔐 Login y roles

El menú principal es:

```
1. Iniciar sesión
2. Crear cuenta
3. Salir
```

Las credenciales se guardan en `login.txt`, único archivo de usuarios del sistema, con el formato:

```
usuario;contraseña;mail;rol
```

* El campo `rol` (`Admin` o `Usuario`) determina qué menú se muestra al iniciar sesión.
* **Usuario:** puede consultar su información y comprar entradas.
* **Admin:** accede a estadísticas más extensas y puede asignar artistas en el lineup.
* Las cuentas de administrador vienen cargadas previamente en el archivo.
* Las cuentas de usuario se crean desde el menú, validando que no se repitan el usuario ni el mail.

### Intentos fallidos de ingreso

* Cada intento fallido se registra en `logs.json` con el email ingresado, el usuario ingresado, la fecha y la causa del fallo.
* **Nunca se guarda la contraseña ingresada.**
* Los intentos se cuentan por usuario/email.
* Al llegar a **3 o más intentos fallidos** se emite una alerta (mensaje en pantalla y marca en el reporte de alertas). La alerta es solo informativa: **no se bloquea el acceso** y el usuario puede seguir intentando.

Ejemplo de `logs.json`:

```json
[
  {
    "email_ingresado": "hola123@gmail",
    "user_ingresado": "Juan_234",
    "fecha": "21-10-2026",
    "causa": "mail incompleto"
  }
]
```

## ✅ Validaciones (expresiones regulares)

Cada formato tiene un mensaje de error que indica qué se espera:

| Dato    | Formato esperado                                     | Dónde se usa                |
|---------|------------------------------------------------------|-----------------------------|
| Usuario | 4 a 15 caracteres: letras, números o guión bajo      | Login                       |
| DNI     | 7 u 8 dígitos                                        | Compra de entradas          |
| Email   | Estructura `nombre@dominio.ext`                      | Login / Compra de entradas  |

## 🗂️ Estructuras de datos

### Diccionarios

* **Diccionario de registros:** recorre `compras.csv` y arma un diccionario por **DNI** (no por usuario, ya que el CSV no almacena el campo usuario), con la cantidad de entradas, el monto total y los IDs de las compras abonadas.
* **Diccionario de acumulador:** almacena los ingresos fallidos de registro.
* **Diccionario de configuración:** carga desde `configuracion.json` las variables fijas (escenarios, horarios y precios de cada tipo de entrada).

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

**`compras.csv`** se actualiza con cada compra realizada:

```
id;fecha;nombre_completo;mail;dni;tipo_entrada;cantidad;monto_final
```

El mail se solicita nuevamente al momento de realizar una compra.

## 🎤 Programación del festival (lineup)

Se mantiene el modelo de datos de la Etapa 1:

* Hasta 30 artistas, identificados por un código único con formato `A-` + dos dígitos (ej: `A-01`).
* 5 escenarios y 8 franjas horarias (13:00 a 20:00).
* **Lineup:** matriz bidimensional de 8 filas × 5 columnas inicializada en `main.py`. Las filas son las franjas horarias y las columnas, los escenarios. Cada celda guarda el código del artista asignado (`A-XX`) o `'.'` si está libre.
* **Artistas:** dos listas paralelas, `codigos` (claves únicas) y `nombre_artistas` (nombres artísticos, en correspondencia por índice).
* **Conteo:** la cantidad de artistas activos se calcula contando los elementos de las listas y recorriendo las celdas de la matriz que difieren de `'.'`.
* Antes de asignar o modificar un artista se valida, en orden: que el código exista y no esté repetido, que el escenario exista, que el horario sea válido, que el artista no esté ya programado en otro lugar y que la combinación escenario/horario esté libre.
* La asignación de artistas es una función exclusiva del rol **Admin**.

> ⚠️ **Persistencia:** la grilla y las listas `codigos` y `nombre_artistas` viven solo en memoria durante la ejecución y se reinician cada vez que se corre el programa. Guardarlas en archivos queda fuera del alcance de la Etapa 2.

## 🎫 Entradas

| Tipo    | Precio    | Cupo máximo | Máx. por operación |
|---------|-----------|-------------|---------------------|
| General | $100.000  | 80          | 6                   |
| VIP     | $250.000  | 20          | 6                   |

* Capacidad total del festival: 100 entradas (80 General + 20 VIP).
* El límite de compra por operación es dinámico: es el menor entre 6 y el stock restante de esa categoría.
* Antes de confirmar una compra se valida disponibilidad y que la cantidad sea un número entero positivo.
* Cada compra registra nombre completo, mail, DNI, tipo de entrada, cantidad y monto final en `compras.csv`. No se almacenan datos de pago.
* El sistema detecta entradas agotadas y avisa cuando queda menos del 20% disponible.

## 🔎 Búsquedas, ordenamientos y rankings

* Búsqueda de artista por código o por nombre, mostrando nombre, escenario y horario asignado.
* Listado de artistas ordenado alfabéticamente (`sorted()`).
* Encuesta al momento de comprar: el usuario vota cuál escenario tiene el mejor lineup (1 al 5). El ranking se arma con una lista paralela a escenarios y se ordena con `.sort()` y `lambda`.
* Uso de listas por comprensión para construir la matriz de `lineup`.

## 📊 Reportes

### Reporte de alertas
Registra en un contador la cantidad de ingresos fallidos. Si un usuario llega a 3 o más intentos, se marca como alerta y se emite un mensaje (solo informativo, no bloquea el acceso).

### Reporte general (`informe.txt`)
Informe final del festival que incluye:

* **Ventas y recaudación:**
  * Entradas General vendidas y su recaudación parcial ($).
  * Entradas VIP vendidas y su recaudación parcial ($).
  * Recaudación total acumulada del festival ($).
  * Porcentaje de ocupación sobre la capacidad global (100 entradas).
  * Estado de disponibilidad por categoría (alertas si hay entradas agotadas o menos del 20% disponible).
* **Programación (lineup):**
  * Total de artistas registrados en el sistema.
  * Franjas horarias/escenarios asignados vs. espacios libres en la matriz.
* **Accesos y alertas:**
  * Total acumulado de intentos fallidos de inicio de sesión.

### Reporte filtrado
Permite consultar las ventas filtrando por tipo de entrada (**General** o **VIP**). La información se lee dinámicamente desde `compras.csv`, por lo que incluye las compras de la sesión actual y de ejecuciones anteriores.

* El sistema solicita el `tipo_entrada` y filtra las filas cuya columna coincida exactamente con la opción elegida.
* Por cada registro muestra: `id`, `fecha`, `nombre_completo`, `mail`, `dni`, `tipo_entrada`, `cantidad` y `monto_final`.
* Al final presenta un resumen con la cantidad total de entradas vendidas, la recaudación total de esa categoría y el porcentaje de ocupación sobre su cupo máximo (80 para General, 20 para VIP).

## ⚠️ Manejo de excepciones

Se usan excepciones para que un error del usuario no finalice el programa sin intención y para informar por qué falló:

* **`FileNotFoundError`:** `compras.csv` y `logs.json` se crean automáticamente si no existen. `configuracion.json` **no** se reemplaza en silencio si falta: se informa el error.
* **Filas CSV con formato incorrecto:** se informan sin perder las filas válidas.
* **`OSError`** en lectura/escritura de archivos y **`ValueError`** en conversiones.

## 🧪 Pruebas unitarias

*A confirmar.*

## 🏗️ Arquitectura

```
proyecto_etapa2/
│
├── main.py             # Punto de entrada; inicializa lineup y listas
├── funciones.py        # Lógica y validaciones (regex, diccionarios, reportes)
├── menu.py             # Menús (principal, Admin y Usuario)
├── archivos.py         # Lectura/escritura de CSV, JSON y TXT
├── logs.json           # Ingresos fallidos
├── configuracion.json  # Escenarios, horarios y entradas
├── compras.csv         # Compras realizadas
├── login.txt           # Usuarios y roles
└── README.md
```

## 🚫 Fuera de este alcance

* Conjuntos y resumen de únicos.
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

## 👥 Integrantes

**Algoritmos y Estructuras de Datos I**

* Iara Reale
* Macarena Prieto
* Solana Cosenza
* Juan Cruz Isola