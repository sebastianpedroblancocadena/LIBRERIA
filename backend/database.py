"""
===================================================================
EduSmart - Capa de Base de Datos Real Relacional (SQL)
===================================================================
Módulo de conexión y operaciones SQL para el Festival de Ciencia 2026.
Soporta SQLite 3 (base de datos relacional local sin configuración extra)
y conexión a PostgreSQL / MySQL mediante DATABASE_URL.
Tablas: productos, clientes, ventas, detalle_ventas, movimientos_inventario.
===================================================================
"""

import sqlite3
import os
import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "edusmart.db")

def get_db_connection():
    """Retorna una conexión a la base de datos relacional SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Permite acceder a columnas por nombre
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """Crea las tablas relacionales y carga los datos iniciales de útiles escolares si están vacías."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Tabla de Productos de Inventario
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id TEXT PRIMARY KEY,
            sku TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL DEFAULT 0,
            image TEXT,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 2. Tabla de Clientes (Estudiantes y Padres de Familia)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT,
            colegio_direccion TEXT,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 3. Tabla de Ventas (Órdenes de Compra)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id TEXT PRIMARY KEY,
            cliente_id INTEGER NOT NULL,
            total REAL NOT NULL,
            metodo_pago TEXT NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            estado TEXT NOT NULL DEFAULT 'Entregado',
            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
        );
    """)

    # 4. Tabla de Detalle de Ventas (Artículos comprados por orden)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS detalle_ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            venta_id TEXT NOT NULL,
            producto_id TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            FOREIGN KEY (venta_id) REFERENCES ventas (id),
            FOREIGN KEY (producto_id) REFERENCES productos (id)
        );
    """)

    # 5. Tabla de Movimientos de Inventario (Kárdex automatizado)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos_inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto_id TEXT NOT NULL,
            tipo TEXT NOT NULL, -- 'VENTA', 'INGRESO', 'AJUSTE'
            cantidad INTEGER NOT NULL,
            motivo TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (producto_id) REFERENCES productos (id)
        );
    """)

    conn.commit()

    # Sembrar productos iniciales si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM productos;")
    if cursor.fetchone()[0] == 0:
        seed_initial_products(conn)

    # Sembrar órdenes demo si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM ventas;")
    if cursor.fetchone()[0] == 0:
        seed_initial_orders(conn)

    conn.close()
    print(f"[OK] Base de datos SQL inicializada exitosamente en: {DB_PATH}")

def seed_initial_products(conn):
    """Inserta el catálogo inicial con las 6 categorías de útiles escolares."""
    initial_products = [
        # 📚 Libros
        ('prod-1', 'LIB-MAT-01', 'Libro de Matemáticas Aplicadas Secundaria', 'Libros', 18.50, 24, 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=600&q=80', 'Texto escolar con ejercicios prácticos, álgebra, geometría y trigonometría para nivel secundario.'),
        ('prod-2', 'LIB-LIT-02', 'Novela Escolar "Cien Años de Soledad" (Ed. Juvenil)', 'Libros', 14.00, 18, 'https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=600&q=80', 'Edición con guía de análisis literario, vocabulario y notas pedagógicas para estudiantes.'),
        ('prod-3', 'LIB-DIC-03', 'Diccionario Escolar de la Lengua Española Ilustrado', 'Libros', 11.50, 15, 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=600&q=80', 'Más de 40,000 definiciones, sinónimos, antónimos y reglas ortográficas actualizadas.'),
        ('prod-4', 'LIB-BIO-04', 'Atlas de Biología y Ciencias Naturales', 'Libros', 16.00, 12, 'https://images.unsplash.com/photo-1532012164546-f432f2e3777f?auto=format&fit=crop&w=600&q=80', 'Guía visual completa sobre anatomía humana, ecosistemas y biodiversidad planetaria.'),

        # 📓 Cuadernos
        ('prod-5', 'CUA-ESP-01', 'Cuaderno Espiral Universitario 100 Hojas Rayado', 'Cuadernos', 3.50, 45, 'https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=600&q=80', 'Tapa dura plastificada, hojas de 75g de alta blancura que no traspasan la tinta.'),
        ('prod-6', 'CUA-CUA-02', 'Cuaderno Cuadriculado 7mm 100 Hojas Cosido', 'Cuadernos', 2.80, 50, 'https://images.unsplash.com/photo-1531346878377-a5be20888e57?auto=format&fit=crop&w=600&q=80', 'Encuadernación cosida resistente al uso rudo escolar, ideal para matemáticas y ciencias.'),
        ('prod-7', 'CUA-DIB-03', 'Cuaderno Block de Dibujo Marquilla 50 Hojas', 'Cuadernos', 4.20, 20, 'https://images.unsplash.com/photo-1600132806370-bf17e65e942f?auto=format&fit=crop&w=600&q=80', 'Papel especial de 120g para lápices de colores, acuarelas ligeras y bocetos artísticos.'),
        ('prod-8', 'CUA-CAL-04', 'Cuaderno Doble Raya Caligrafía y Escritura', 'Cuadernos', 2.20, 35, 'https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=600&q=80', 'Especial para el desarrollo de la motricidad fina y caligrafía en primaria y secundaria.'),

        # ✏️ Lápices
        ('prod-9', 'LAP-GRA-01', 'Caja de Lápices Grafito HB Faber-Castell (12 Uds)', 'Lápices', 4.80, 40, 'https://images.unsplash.com/photo-1585336261026-8c4600216b3f?auto=format&fit=crop&w=600&q=80', 'Mina protegida contra roturas mediante proceso de encolado SV. Escritura suave y precisa.'),
        ('prod-10', 'LAP-COL-02', 'Lápices de Colores x24 Largos Prismacolor Junior', 'Lápices', 8.90, 28, 'https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?auto=format&fit=crop&w=600&q=80', 'Pigmentos vivos e intensos, mina suave de 3.3mm que permite mezclas y degradados uniformes.'),
        ('prod-11', 'LAP-POR-03', 'Portaminas Metálico Ergonómico 0.5mm + Minas 2B', 'Lápices', 3.90, 18, 'https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?auto=format&fit=crop&w=600&q=80', 'Cuerpo metálico con agarre antideslizante y borrador integrado libre de látex.'),
        ('prod-12', 'LAP-BIC-04', 'Lápiz Bicolor Rojo / Azul para Correcciones (Pack x3)', 'Lápices', 2.10, 30, 'https://images.unsplash.com/photo-1596495578065-6e0763fa1178?auto=format&fit=crop&w=600&q=80', 'Imprescindible para subrayados, revisión de tareas y mapas geográficos escolares.'),

        # 🖊️ Lapiceros
        ('prod-13', 'LPC-TRI-01', 'Set de Lapiceros Clásicos 4 Colores (Azul, Negro, Rojo, Verde)', 'Lapiceros', 2.50, 60, 'https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?auto=format&fit=crop&w=600&q=80', 'Punta media de 1.0mm, flujo constante de tinta que garantiza escritura sin manchas.'),
        ('prod-14', 'LPC-GEL-02', 'Lapicero de Tinta Gel 0.5mm Negro Secado Rápido', 'Lapiceros', 1.80, 45, 'https://images.unsplash.com/photo-1569683795645-b62e50fbf103?auto=format&fit=crop&w=600&q=80', 'Tinta gel ultra fluida indeleble, perfecta para exámenes, apuntes limpios y firmas.'),
        ('prod-15', 'LPC-ROL-03', 'Pluma Rollerball Tinta Líquida Azul Real Pilot', 'Lapiceros', 3.20, 22, 'https://images.unsplash.com/photo-1585336261026-8c4600216b3f?auto=format&fit=crop&w=600&q=80', 'Visor transparente de nivel de tinta, punta de carburo de tungsteno indeformable.'),
        ('prod-16', 'LPC-RES-04', 'Set de Resaltadores Pastel x6 Colores Suaves', 'Lapiceros', 5.40, 25, 'https://images.unsplash.com/photo-1596495578065-6e0763fa1178?auto=format&fit=crop&w=600&q=80', 'Punta biselada para trazos de 2mm y 5mm. Tinta al agua ecológica que no atraviesa el papel.'),

        # 📏 Reglas
        ('prod-17', 'REG-JUE-01', 'Juego Geométrico Escolar Completo 4 Piezas (30cm)', 'Reglas', 4.50, 35, 'https://images.unsplash.com/photo-1580974852861-c381510bc98a?auto=format&fit=crop&w=600&q=80', 'Incluye regla de 30cm, escuadra 45°, cartabón 60° y transportador de 180° en estuche protector.'),
        ('prod-18', 'REG-ACE-02', 'Regla Metálica de Acero Inoxidable Graduada 30cm', 'Reglas', 3.20, 28, 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=600&q=80', 'Graduación milimétrica grabada al ácido, resistente a golpes y cortes con cutter.'),
        ('prod-19', 'REG-TRA-03', 'Transportador Circular 360° Acrílico Transparente', 'Reglas', 2.10, 30, 'https://images.unsplash.com/photo-1580974852861-c381510bc98a?auto=format&fit=crop&w=600&q=80', 'Visión completa para cálculos precisos de ángulos en matemáticas, física y dibujo técnico.'),
        ('prod-20', 'REG-ESC-04', 'Escalímetro Triangular Técnico Profesional', 'Reglas', 6.80, 14, 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=600&q=80', '6 escalas normalizadas para estudiantes de secundaria avanzada, diseño y arquitectura.'),

        # 📁 Carpetas
        ('prod-21', 'CAR-ARC-01', 'Archivador de Palanca Tamaño Oficio Dos Anillas', 'Carpetas', 5.50, 26, 'https://images.unsplash.com/photo-1586075010923-2dd4570fb338?auto=format&fit=crop&w=600&q=80', 'Cartón extra grueso forrado en PVC lavable, mecanismo niquelado con cantoneras metálicas.'),
        ('prod-22', 'CAR-FUE-02', 'Carpeta Fuelle Acordeón con 12 Divisiones de Colores', 'Carpetas', 6.20, 19, 'https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=600&q=80', 'Permite clasificar todas las materias escolares en un solo lugar con pestañas identificadoras.'),
        ('prod-23', 'CAR-SOB-03', 'Carpeta Plástica Tipo Sobre con Broche Escolar (Pack x3)', 'Carpetas', 3.10, 45, 'https://images.unsplash.com/photo-1586075010923-2dd4570fb338?auto=format&fit=crop&w=600&q=80', 'Polipropileno translúcido impermeable que protege tareas y trabajos contra lluvia y manchas.'),
        ('prod-24', 'CAR-MAN-04', 'Fólder Manila Reforzado Tamaño Carta (Paquete x10)', 'Carpetas', 2.80, 50, 'https://images.unsplash.com/photo-1586075010923-2dd4570fb338?auto=format&fit=crop&w=600&q=80', 'Pestaña superior reforzada para entrega formal de monografías e informes escolares.')
    ]
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO productos (id, sku, name, category, price, stock, image, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, initial_products)
    conn.commit()

def seed_initial_orders(conn):
    """Inserta órdenes iniciales de prueba para el festival."""
    cursor = conn.cursor()
    
    # Insertar clientes de prueba con el número de WhatsApp oficial
    cursor.execute("""
        INSERT INTO clientes (nombre, telefono, correo, colegio_direccion)
        VALUES ('Carlos Villarroel', '+591 62559281', 'carlos.v@gmail.com', 'Colegio Franco Boliviano - 4to Sec.');
    """)
    c1_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO clientes (nombre, telefono, correo, colegio_direccion)
        VALUES ('Mariana Gutierrez', '+591 62559281', 'mariana.g@outlook.com', 'Col. Alemán - 1ro Secundaria');
    """)
    c2_id = cursor.lastrowid

    # Insertar ventas
    cursor.execute("""
        INSERT INTO ventas (id, cliente_id, total, metodo_pago, fecha, estado)
        VALUES ('ORD-2026-9142', ?, 37.90, 'QR / Transferencia', '2026-09-09 14:32:10', 'Entregado');
    """, (c1_id,))
    
    cursor.execute("""
        INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario)
        VALUES ('ORD-2026-9142', 'prod-1', 1, 18.50),
               ('ORD-2026-9142', 'prod-5', 3, 3.50),
               ('ORD-2026-9142', 'prod-10', 1, 8.90);
    """)

    cursor.execute("""
        INSERT INTO ventas (id, cliente_id, total, metodo_pago, fecha, estado)
        VALUES ('ORD-2026-9141', ?, 25.10, 'Tarjeta Débito/Crédito', '2026-09-09 16:45:22', 'Entregado');
    """, (c2_id,))
    
    cursor.execute("""
        INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario)
        VALUES ('ORD-2026-9141', 'prod-9', 2, 4.80),
               ('ORD-2026-9141', 'prod-17', 1, 4.50),
               ('ORD-2026-9141', 'prod-21', 2, 5.50);
    """)

    conn.commit()

if __name__ == "__main__":
    init_db()
