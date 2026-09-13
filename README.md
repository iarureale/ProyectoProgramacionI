 🎵 Overpalooza

Proyecto integrador desarrollado en **Python** para la materia **Algoritmos y Estructuras de Datos I**.

📌 Descripción

**Overpalooza** es un sistema de gestión para un festival de música, con dos áreas independientes que comparten el dominio del festival pero usan estructuras de datos propias:

* **Programación del festival:** carga de artistas, asignación a escenarios y franjas horarias, y consulta de la grilla.
* **Venta de entradas:** comercialización de entradas General y VIP, control de disponibilidad y cálculo de indicadores económicos.

El sistema se maneja a través de un único menú principal (no hay login ni distinción de roles).

## 🎤 Programación del festival

* Hasta 30 artistas, identificados por un código único con formato `A-` + dos dígitos (ej: `A-01`).
* 5 escenarios fijos: `McStage`, `PStage`, `FIATStage`, `FlowStage`, `SanStage`.
* Grilla hora a hora de 13:00 a 20:00 (8 franjas horarias).
* La programación se representa con una matriz `lineup[horario][escenario]`, donde cada celda guarda el código del artista asignado (o `""` si está libre).
* Antes de asignar o modificar un artista en la grilla se valida, en orden: que el código exista y no esté repetido, que el escenario exista, que el horario sea válido, que el artista no esté ya programado en otro lugar, y que la combinación escenario/horario esté libre.

## 🎫 Entradas

| Tipo    | Precio    | Cupo máximo | Máx. por operación |
|---------|-----------|-------------|---------------------|
| General | $100.000  | 80          | 6                   |
| VIP     | $250.000  | 20          | 6                   |

* Capacidad total del festival: 100 entradas (80 General + 20 VIP).
* El límite de compra por operación es dinámico: es el menor entre 6 y el stock restante de esa categoría.
* Antes de confirmar una compra se valida disponibilidad y que la cantidad sea un número entero positivo.
* No se almacenan datos personales del comprador ni datos de pago; solo se registran tipo de entrada, cantidad e importe.
* El sistema detecta entradas agotadas (General o VIP en 0) y avisa cuando queda menos del 20% de entradas disponibles en total.

## 🔎 Búsquedas, ordenamientos y rankings

* Búsqueda de artista por código o por nombre, mostrando nombre, escenario y horario asignado.
* Listado de artistas ordenado alfabéticamente (`sorted()`).
* Encuesta al momento de comprar: el usuario vota cuál escenario tiene el mejor lineup (1 al 5). El ranking se arma con una lista paralela a escenarios y se ordena con `.sort()` y `lambda`.
* Uso de listas por comprensión para construir la matriz de `lineup`.

## 📊 Informes

1. Grilla completa del festival (escenarios × horarios × artistas).
2. Entradas vendidas por tipo (General / VIP).
3. Recaudación total y por tipo de entrada.
4. Porcentaje de entradas vendidas sobre la capacidad total.
5. Informe de entradas agotadas o con baja disponibilidad.

## 📋 Menú principal

```
1. Consultar información del festival
2. Buscar artista
3. Consultar grilla
4. Comprar entradas
5. Modificar programación
6. Estadísticas e informes
7. Salir
```

## ⚙️ Restricciones de implementación

* No se utiliza `while True` ni `try/except`.
* No hay bases de datos, archivos, envío de mails, aplicación web ni logins.
* Quedan fuera del alcance: pagos reales, almacenamiento de tarjetas, entradas digitales/QR, devoluciones, control de ingreso al predio y múltiples días de festival.

▶️ Ejecución

Clonar el repositorio:

```bash
git clone https://github.com/iarureale/ProyectoProgramacionI.git
```

Luego ejecutar `main/main.py` con Python.

👥 Integrantes

**Algoritmos y Estructuras de Datos I**

* Iara Reale
* Macarena Prieto
* Solana Cosenza
* Juan Cruz Isola
