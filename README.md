🎵 Overpalooza

Proyecto desarrollado en **Python** para la materia **Algoritmos y Estructuras de Datos I**.

📌 Descripción

**Overpalooza** es un sistema para gestionar un festival de música. Cuenta con dos menús:

* **Usuario:** permite consultar información del festival, buscar artistas, consultar la grilla y comprar entradas.
* **Administrador:** permite gestionar artistas y la programación, consultar entradas vendidas y obtener estadísticas económicas.

🎫 Entradas

El sistema cuenta con dos tipos de entradas:

* **General:** $100.000 — máximo 80 entradas.
* **VIP:** $250.000 — máximo 20 entradas.

Cada usuario puede comprar hasta **6 entradas por operación**.

## 🎤 Festival

* 30 artistas.
* 5 escenarios.
* Horarios de 13:00 a 01:00.
* Programación organizada mediante una matriz de **horario, escenario y artista**.

## 🔐 Administrador

El acceso al menú de administrador está protegido mediante una contraseña hardcodeada:

```text
admin
```

Desde este menú se pueden cargar y eliminar artistas, asignar escenarios y horarios, modificar la programación y consultar estadísticas y recaudación.

📊 Estadísticas

El sistema permite calcular:

* Porcentaje de entradas vendidas.
* Recaudación total.
* Cantidad y recaudación de entradas VIP.
* Cantidad y recaudación de entradas Generales.
* Rankings económicos.

⚙️ Validaciones

El sistema valida los datos ingresados durante la compra y evita errores como datos vacíos, documentos inválidos, mails incorrectos y compras superiores a 6 entradas.

▶️ Ejecución

Clonar el repositorio:

```bash
git clone https://github.com/iarureale/ProyectoProgramacionI.git
```

Luego ejecutar el archivo principal del proyecto con Python.

👥 Integrantes

**Programación I**

* Iara Reale
* Macarena Prieto
* Solana Cosenza
* Juan Cruz Isola
* Araceli Sinche
* Molinari
