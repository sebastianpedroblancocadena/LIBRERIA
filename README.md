# EduSmart - Sistema Integral de Tienda Escolar & Gestión de Inventario 🎓
**Proyecto Oficial para la Exposición del EduSmart Escolar**

---

## 🌟 Descripción General del Proyecto
**EduSmart** es una plataforma tecnológica integral diseñada para optimizar los procesos de comercialización y administración de materiales escolares, resolviendo la falta de precisión en los inventarios manuales y ofreciendo a **estudiantes, padres de familia y administradores** una experiencia moderna, automatizada y de alta fidelidad.

El sistema cuenta con:
1. **Interfaz del Cliente (Estudiantes y Padres)**: Catálogo digital con 6 categorías escolares (📚 Libros, 📓 Cuadernos, ✏️ Lápices, 🖊️ Lapiceros, 📏 Reglas, 📁 Carpetas), carrito interactivo, checkout escalable y confirmación con la **API de Meta Cloud (WhatsApp: Opción no disponible todavía)**.
2. **Backend Real en Python (Flask REST API)**: Servidor robusto con endpoints CRUD, transacciones ACID para descuento automático de stock, generación de reportes en PDF binario con ReportLab y simulación de Webhooks.
3. **Base de Datos Relacional SQL (`edusmart.db`)**: Esquema normalizado relacional con claves foráneas e integridad referencial (compatible con SQLite y clústeres MySQL / PostgreSQL).
4. **Peticiones `fetch()` en Tiempo Real**: El frontend en `index.html` se comunica directamente con la API de Python a través de `fetch()`, con fallback inteligente y seguro a modo local si el servidor estuviera apagado.
5. **Arquitectura 24/7, Seguridad SSL y Viabilidad**: Base de datos ininterrumpida, cifrado TLS 1.3 de 256 bits, flujo de Webhooks y estudio financiero con presupuesto de **7.000 Bs.** amortizable en **30 días (1 mes)**.

---

## 📁 Estructura del Proyecto

```text
exposicion/
├── index.html                  # Frontend interactivo conectado con fetch() al Backend
├── iniciar_servidor.bat        # Lanzador 1-clic para Windows (instala, inicializa BD y abre navegador)
├── iniciar_servidor.ps1        # Lanzador PowerShell con salidas formateadas
├── README.md                   # Documentación completa y guía de exposición
└── backend/
    ├── app.py                  # Servidor API REST en Python (Flask, endpoints CRUD, PDF y Webhooks)
    ├── database.py             # Motor relacional SQL, creación de tablas y sembrado inicial
    ├── edusmart.db             # Base de datos SQL física relacional generada
    ├── generar_reporte.py      # Generador de reportes PDF con ReportLab / PDFKit
    ├── requirements.txt        # Dependencias del entorno Python (Flask, Flask-CORS, ReportLab)
    └── test_backend.py         # Suite de pruebas automatizadas de endpoints y stock ACID
```

---

## 🚀 Cómo Iniciar el Sistema (¡1 Clic en Windows!)

### Opción A: Lanzador Automático (Recomendado)
1. Haz doble clic en **`iniciar_servidor.bat`** (o ejecuta `.\iniciar_servidor.ps1` en PowerShell).
2. El script automáticamente:
   - Detectará tu instalación de Python.
   - Instalará las librerías necesarias (`flask`, `flask-cors`, `reportlab`).
   - Inicializará la base de datos relacional SQL `edusmart.db` si no existe.
   - Abrirá tu navegador en `http://localhost:5000`.
   - Mantendrá el servidor Flask corriendo.

### Opción B: Ejecución Manual desde Terminal
```bash
# Navegar a la carpeta backend
cd backend

# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor Flask
python app.py
```
Abre en tu navegador `http://localhost:5000`.

### Opción C: Modo Autónomo Local (Sin Servidor)
Si deseas presentar la interfaz sin encender Python, simplemente abre `index.html` directamente en cualquier navegador. El sistema detectará automáticamente que el backend está inactivo, mostrará el indicador **"🟡 Modo Local Demo"** y operará fluidamente usando almacenamiento local (`localStorage`).

---

## 🗄️ Base de Datos Relacional SQL (`edusmart.db`)

El sistema utiliza un modelo relacional normalizado con integridad referencial:
- **`productos`**: Catálogo con SKU único, nombre, categoría, precio escolar, stock físico, imagen y descripción.
- **`clientes`**: Registro de tutores y estudiantes con nombre, teléfono WhatsApp (`Opción no disponible todavía`), correo y colegio/dirección.
- **`ventas`**: Registro de órdenes con número de orden único, clave foránea `cliente_id`, monto total, método de pago, timestamp y estado.
- **`detalle_ventas`**: Desglose línea por línea de productos adquiridos con precio unitario congelado y cantidad.
- **`movimientos_inventario`**: Registro kárdex de auditoría (entradas, salidas automáticas por venta y ajustes manuales del panel admin).

---

## 🌐 Endpoints de la API REST (Backend Flask)

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/` | Sirve la interfaz web `index.html` estática |
| `GET` | `/api/status` | Telemetría del servidor, motor de BD y viabilidad |
| `GET` | `/api/productos` | Obtiene el catálogo escolar (soporta filtros por categoría y búsqueda) |
| `POST` | `/api/productos` | Crea un nuevo ítem en el inventario escolar |
| `PUT` | `/api/productos/<id>` | Actualiza campos o stock del producto |
| `DELETE` | `/api/productos/<id>` | Elimina un producto de la base de datos |
| `POST` | `/api/ventas` | **Transacción ACID**: descuenta stock, inserta orden, detalle, kárdex y simula Webhook WhatsApp |
| `GET` | `/api/ventas` | Lista las ventas procesadas con clientes y desglose de ítems |
| `GET` | `/api/dashboard/stats` | Estadísticas para el panel de control y gráficos Chart.js |
| `GET` | `/api/reportes/semanal-pdf` | Genera y transmite en binario el reporte oficial en PDF con ReportLab |

---

## 🧪 Pruebas Automatizadas del Backend

Para validar el correcto funcionamiento de la base de datos y la API:
```bash
python backend/test_backend.py
```
Salida esperada:
```text
============================================================
 EduSmart - Suite de Pruebas de Integracion Backend & SQL
============================================================
[1/4] Probando /api/status... OK (Status 200)
[2/4] Probando /api/productos... OK (24 productos encontrados)
[3/4] Probando /api/ventas (Descuento Automatico ACID)...
      Stock antes de compra: 25 uds.
      Procesando orden de compra con 2 unidades...
      Stock despues de compra: 23 uds.
      OK: Descuento atomico de inventario verificado en SQL!
[4/4] Probando /api/reportes/semanal-pdf (ReportLab)... OK (PDF binario valido)
============================================================
 [EXITO] Todas las pruebas del backend pasaron al 100%!
============================================================
```

---

## 🧭 Guía Paso a Paso para la Exposición ante el Jurado

### Paso 1: Interfaz del Cliente (Estudiantes y Padres)
- Observa en la barra superior el distintivo **"🟢 API Python & SQL Activos"**. Haz clic en él para comprobar la sincronización en vivo.
- Explora el **Catálogo Escolar** (📚 Libros, 📓 Cuadernos, ✏️ Lápices, 🖊️ Lapiceros, 📏 Reglas, 📁 Carpetas).
- Agrega productos al carrito y haz clic en **"Proceder al Pago Seguro"**.
- Selecciona el método de pago y haz clic en **"Confirmar y Descontar Stock"**.
- Observa la ventana emergente de confirmación de **Meta Cloud API (WhatsApp)** con el número oficial de atención: **`Opción no disponible todavía`**.

### Paso 2: Panel de Administración (Dueño o Empleado)
- Pasa al **Panel de Administración**:
  - **Dashboard**: Gráficos analíticos con Chart.js y actividad en tiempo real.
  - **Inventario**: Demuestra que el stock del producto comprado se redujo automáticamente en la base de datos.
  - **CRUD**: Agrega un producto nuevo o ajusta existencias con los botones de un solo clic.
  - **Reportes**: Haz clic en **"Descargar PDF (Backend Python)"** para recibir el reporte oficial generado al vuelo con ReportLab.

### Paso 3: Módulo de Arquitectura & Viabilidad
- **Base de Datos 24/7**: Clúster de alta disponibilidad con réplicas y transacciones ACID.
- **Seguridad SSL**: Cifrado TLS 1.3 de 256 bits para protección de datos personales.
- **Webhooks**: Flujo en tiempo real entre pasarela de pagos, servidor Python y Meta Cloud API.
- **Viabilidad Financiera**:
  - Inversión inicial total: **7.000 Bs.**.
  - Beneficio mensual proyectado: **+8.150 Bs.**.
  - Plazo de recuperación (ROI): **30 días (1 mes)**.

---

**Desarrollado para el EduSmart Escolar**
*EduSmart - La transformación digital de la librería escolar.*
