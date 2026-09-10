"""
===================================================================
EduSmart - Script de Generación de Reportes PDF con Python
===================================================================
Herramienta en Python para generar y evaluar reportes semanales
de ventas e inventario en formato PDF (utilizando PDFKit / ReportLab).
Presentación para el Festival de Ciencia 2026.
===================================================================
"""

import sys
import os
import datetime

def generar_reporte_con_pdfkit(archivo_salida="reporte_semanal_pdfkit.pdf"):
    """
    Genera el reporte utilizando la librería pdfkit (Python wrapper para wkhtmltopdf).
    Cumple con el requisito técnico especificado en el proyecto.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; color: #1e293b; }}
            .header {{ background-color: #1e3a8a; color: white; padding: 25px; border-radius: 10px; }}
            h1 {{ margin: 0; font-size: 24px; }}
            .sub {{ font-size: 13px; opacity: 0.9; margin-top: 5px; }}
            .section {{ margin-top: 30px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
            th, td {{ border: 1px solid #cbd5e1; padding: 8px 12px; text-align: left; font-size: 12px; }}
            th {{ background-color: #f1f5f9; font-weight: bold; color: #0f172a; }}
            .kpi-box {{ background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px; border-radius: 8px; margin-bottom: 20px; }}
            .badge-low {{ background: #fef3c7; color: #92400e; font-weight: bold; padding: 2px 6px; border-radius: 4px; }}
            .footer {{ margin-top: 50px; font-size: 11px; color: #64748b; border-top: 1px solid #e2e8f0; padding-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>EDUSMART - REPORTE SEMANAL DE INVENTARIO Y VENTAS</h1>
            <div class="sub">Festival de Ciencia 2026 | Sistema de Gestión Escolar con Backend en Python</div>
        </div>

        <div class="section">
            <div class="kpi-box">
                <strong>Resumen Ejecutivo:</strong><br>
                • Inversión del Proyecto: <strong>$7,000 USD</strong> netos con retorno estimado en 30 días.<br>
                • Disponibilidad del Sistema: <strong>Base de datos PostgreSQL 24/7</strong> con certificación SSL activa.<br>
                • Sincronización: <strong>Webhooks automáticos</strong> con la API de Meta Cloud (WhatsApp).
            </div>

            <h3>1. Estado del Inventario de Útiles Escolares</h3>
            <table>
                <thead>
                    <tr>
                        <th>SKU</th>
                        <th>Producto</th>
                        <th>Categoría</th>
                        <th>Precio Unitario</th>
                        <th>Stock Actual</th>
                        <th>Alerta</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>LIB-MAT-01</td>
                        <td>Libro de Matemáticas Aplicadas Secundaria</td>
                        <td>Libros</td>
                        <td>$18.50</td>
                        <td>24 unidades</td>
                        <td>Óptimo</td>
                    </tr>
                    <tr>
                        <td>CUA-ESP-01</td>
                        <td>Cuaderno Espiral Universitario 100 Hojas</td>
                        <td>Cuadernos</td>
                        <td>$3.50</td>
                        <td>45 unidades</td>
                        <td>Óptimo</td>
                    </tr>
                    <tr>
                        <td>LAP-GRA-01</td>
                        <td>Caja de Lápices Grafito HB Faber-Castell</td>
                        <td>Lápices</td>
                        <td>$4.80</td>
                        <td>40 unidades</td>
                        <td>Óptimo</td>
                    </tr>
                    <tr>
                        <td>REG-ESC-04</td>
                        <td>Escalímetro Triangular Técnico Profesional</td>
                        <td>Reglas</td>
                        <td>$6.80</td>
                        <td>3 unidades</td>
                        <td><span class="badge-low">Stock Crítico</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="footer">
            Generado automáticamente por el motor Python PDFKit | Fecha de emisión: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        </div>
    </body>
    </html>
    """

    try:
        import pdfkit
        pdfkit.from_string(html_content, archivo_salida)
        print(f"[OK] Reporte PDF generado exitosamente con PDFKit: {archivo_salida}")
    except ImportError:
        print("[AVISO] 'pdfkit' no está instalado en este entorno de Python.")
        print("Para instalar: pip install pdfkit (y tener wkhtmltopdf en el PATH del sistema).")
        # Generamos un archivo HTML equivalente para que el usuario pueda abrirlo o convertirlo
        html_salida = archivo_salida.replace(".pdf", ".html")
        with open(html_salida, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[OK] Se ha generado la plantilla HTML lista para imprimir como PDF: {html_salida}")

if __name__ == "__main__":
    generar_reporte_con_pdfkit()
