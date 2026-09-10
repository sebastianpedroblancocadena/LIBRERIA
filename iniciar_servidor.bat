@echo off
chcp 65001 >nul
title EduSmart - Servidor Python & Base de Datos SQL (Festival de Ciencia 2026)
echo =========================================================================
echo       EDUSMART - SISTEMA DE TIENDA ESCOLAR & GESTION DE INVENTARIO
echo                   Festival de Ciencia 2026
echo =========================================================================
echo.
echo [*] Verificando entorno de ejecucion de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] No se encontro Python en el sistema.
    echo Por favor instala Python 3.9+ desde python.org y asegurate de marcar
    echo "Add Python to PATH".
    pause
    exit /b 1
)

echo [*] Entorno de Python detectado correctamente.
echo [*] Verificando e instalando dependencias (Flask, Flask-CORS, ReportLab)...
python -m pip install -r backend\requirements.txt --quiet

echo.
echo [*] Inicializando Base de Datos Relacional SQL (edusmart.db)...
python -c "import sys; sys.path.append('backend'); from database import init_db; init_db()"

echo.
echo =========================================================================
echo  [OK] SERVIDOR INICIADO EN: http://localhost:5000
echo  [OK] BASE DE DATOS SQL: edusmart.db (Transacciones ACID activas)
echo  [OK] WHATSAPP OFICIAL: +591 62559281 (Meta Cloud API Webhook)
echo =========================================================================
echo.
echo Abriendo EduSmart en tu navegador web predeterminado...
timeout /t 2 >nul
start http://localhost:5000

echo.
echo Presiona Ctrl + C en esta ventana para detener el servidor.
echo.
python backend\app.py
pause
