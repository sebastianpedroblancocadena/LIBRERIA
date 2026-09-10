# EduSmart - Sistema Integral de Tienda Escolar & Gestión de Inventario 🎓
**Proyecto Oficial para la Exposición del Festival de Ciencia 2026**

---

## 🌟 Descripción General del Proyecto
EduSmart es una solución tecnológica integral diseñada para resolver la falta de precisión en los inventarios escolares y ofrecer a **estudiantes y padres de familia** una experiencia moderna, rápida y segura para la compra de útiles escolares en línea.

El sistema se compone de tres núcleos funcionales:
1. **Interfaz del Cliente (Estudiantes y Padres)**: Tienda web intuitiva, responsiva (computadoras y celulares), con catálogo escolar, carrito de compras, checkout escalable y notificaciones inmediatas a través de la **API de Meta Cloud (WhatsApp)**.
2. **Panel de Administración (Dueño o Empleado)**: Sistema privado con backend en **Python**, control de inventario con **descuento automático de stock** en tiempo real, registro seguro de clientes y ventas, y generador de **reportes semanales en formato PDF** (simulación y motor PDFKit).
3. **Arquitectura y Seguridad**: Base de datos ininterrumpida **24/7** (MySQL / PostgreSQL), seguridad mediante certificados **SSL/TLS de 256 bits**, sincronización con **Webhooks** y análisis de viabilidad financiera con un presupuesto de **$7,000 USD netos** amortizables en **1 mes (30 días)**.

---

## 📁 Estructura del Proyecto

```text
exposicion/
├── index.html                  # Plataforma web interactiva completa (Cliente, Admin y Arquitectura)
├── backend/
│   ├── app.py                  # Servidor API REST en Python (Flask, endpoints CRUD, Webhooks)
│   ├── generar_reporte.py      # Herramienta en Python para compilar reportes en PDF con PDFKit
│   └── requirements.txt        # Dependencias del entorno Python
└── README.md                   # Documentación técnica y guía de exposición
```

---

## 🚀 Cómo Ejecutar la Aplicación

### 1. Ejecución Directa en el Navegador (Recomendada para la Presentación)
La aplicación web principal es 100% autónoma y no requiere compiladores ni configuraciones complejas:
1. Dirígete a la carpeta `exposicion/`.
2. Haz doble clic en el archivo `index.html` o ábrelo con Google Chrome, Microsoft Edge, Firefox o cualquier navegador moderno.
3. ¡Listo! Puedes navegar libremente entre:
   - **🏪 Tienda del Cliente**
   - **🔐 Panel de Administración**
   - **🏛️ Arquitectura & Viabilidad**

### 2. Ejecución del Backend en Python (Opcional para Demostración al Jurado)
Si los evaluadores del festival solicitan ver la API de Python en ejecución:
```bash
# Navegar a la carpeta del backend
cd "c:\Users\SEBASTIAN BLANCO\Downloads\trabajos\FESTIVAL DE CIENCIA\INFORMACION (documentos)\exposicion\backend"

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor Flask
python app.py
```
El servidor quedará disponible en `http://localhost:5000` con endpoints listos:
- `GET /api/productos`: Consulta del catálogo.
- `POST /api/ventas`: Registro de ventas con descuento automático de stock.
- `GET /api/reportes/semanal-pdf`: Generación del reporte en PDF.

---

## 🧭 Guía para la Exposición ante el Jurado

### Paso 1: Interfaz del Cliente (Estudiantes y Padres)
- **Página de Inicio (Home)**:
  - Muestra el **banner llamativo con imágenes de útiles escolares** y haz clic en el botón principal **"Comprar en línea"**.
  - Prueba los botones de **compartir en redes sociales** (WhatsApp, Facebook, X y enlace copiado).
- **Catálogo de Productos 🛒**:
  - Demuestra las 6 categorías de útiles escolares:
    - 📚 **Libros** (Textos secundarios, novelas juveniles, atlas)
    - 📓 **Cuadernos** (Espirales, cosidos, dibujo, caligrafía)
    - ✏️ **Lápices** (Grafito HB, cajas de 24 colores, portaminas)
    - 🖊️ **Lapiceros** (Bolígrafos 4 colores, tinta gel, rollerball)
    - 📏 **Reglas** (Juego geométrico de 4 piezas, reglas de acero, transportadores)
    - 📁 **Carpetas** (Archivadores de palanca, carpetas con broche, de fuelle)
  - Utiliza la **barra de búsqueda en vivo** escribiendo por ejemplo *"cuaderno"* o *"lapicero"*.
  - Filtra por categorías utilizando los botones interactivos.
- **Carrito y Checkout Escalable 💳**:
  - Añade 2 o 3 productos al carrito. Observa cómo se actualiza el contador dinámico en tiempo real.
  - Abre el carrito, ajusta las cantidades (+ / -) y haz clic en **"Proceder al Pago Seguro"**.
  - Completa los datos del estudiante/padre y selecciona un método de pago (Pago QR, Tarjeta con SSL o Efectivo contraentrega).
  - Haz clic en **"Confirmar y Descontar Stock"**.
- **Notificación Meta Cloud API (WhatsApp)**:
  - Observa la ventana emergente que simula el mensaje oficial de **WhatsApp Business con ticket de compra**, número de orden, resumen de ítems y botón directo para abrir la conversación en WhatsApp.

### Paso 2: Panel de Administración (Dueño o Empleado)
- Haz clic en la pestaña **"Panel de Administración"** en la barra superior.
- **Dashboard Principal 🖥️**:
  - Muestra los indicadores clave (Ingresos totales, Ventas acumuladas, Stock bajo y Catálogo activo).
  - Explica los **gráficos interactivos de ventas semanales y demanda por categoría** (Chart.js).
  - En la sección inferior, muestra el **Feed de Automatización**: la compra recién hecha aparece sincronizada inmediatamente.
- **Módulo de Gestión de Inventario 📦**:
  - Demuestra que el producto comprado tiene **menos unidades de stock** (¡automatización confirmada!).
  - Utiliza los botones de **Ajuste Rápido (+ / -)** para actualizar existencias en un solo clic.
  - Haz clic en **"Agregar Nuevo Producto"** para demostrar el CRUD completo.
- **Módulo de Clientes y Ventas 👥**:
  - Revisa la tabla con el historial de compras, método de pago y datos del tutor o estudiante.
- **Módulo de Reportes 📊**:
  - Haz clic en **"Descargar Reporte en PDF"**. Se descargará inmediatamente un documento PDF profesional con membrete, tabla de ventas, estado del inventario y firmas oficiales.

### Paso 3: Arquitectura, Seguridad y Viabilidad
- Pasa a la pestaña **"Arquitectura & Viabilidad"**:
  - **Base de Datos 24/7**: Explica el clúster relacional MySQL/PostgreSQL con disponibilidad permanente y transacciones ACID.
  - **Seguridad SSL 🔒**: Explica el túnel cifrado TLS de 256 bits para proteger los datos de menores y pagos.
  - **Sincronización Webhooks**: Muestra el diagrama de flujo interactivo que conecta al cliente, servidor Python, base de datos y WhatsApp.
  - **Viabilidad Financiera ($7,000 USD y ROI en 1 mes)**:
    - Muestra la tabla con el desglose exacto de los $7,000 USD netos.
    - Demuestra cómo los **+$8,150 USD de beneficio mensual estimado** (por incremento de ventas online y ahorro de pérdidas de inventario) permiten amortizar el 100% de la inversión en solo **30 días**.

---

## 🛠️ Tecnologías Empleadas
- **Frontend**: HTML5 Semántico, CSS3, JavaScript Moderno (ES6+), **Tailwind CSS**.
- **Visualización & Métricas**: **Chart.js**.
- **Generación de Reportes**: **jsPDF** & AutoTable (Frontend) y **PDFKit** / ReportLab (Backend en Python).
- **Backend**: **Python 3.11** + **Flask**.
- **Comunicaciones**: Simulación de **Meta Cloud API** (WhatsApp Webhooks).
- **Iconografía & Tipografía**: FontAwesome 6.5, Google Fonts (*Poppins* e *Inter*).
