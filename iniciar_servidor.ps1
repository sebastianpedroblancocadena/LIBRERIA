# =========================================================================
# EduSmart - Launcher PowerShell (Festival de Ciencia 2026)
# =========================================================================
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "=========================================================================" -ForegroundColor Cyan
Write-Host "      EDUSMART - SISTEMA DE TIENDA ESCOLAR & GESTION DE INVENTARIO      " -ForegroundColor Yellow
Write-Host "                  Festival de Ciencia 2026                              " -ForegroundColor White
Write-Host "=========================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Verificar Python
Write-Host "[*] Verificando entorno de Python..." -ForegroundColor Gray
try {
    $pyVer = python --version 2>&1
    Write-Host "[OK] $pyVer detectado." -ForegroundColor Green
} catch {
    Write-Host "[ERROR] No se pudo encontrar Python en el sistema." -ForegroundColor Red
    Write-Host "Por favor instala Python 3.9 o superior y agregalo al PATH." -ForegroundColor Yellow
    Pause
    Exit
}

# 2. Instalar dependencias
Write-Host "[*] Verificando dependencias en backend\requirements.txt..." -ForegroundColor Gray
python -m pip install -r backend\requirements.txt --quiet

# 3. Inicializar Base de Datos SQL
Write-Host "[*] Verificando e inicializando base de datos relacional SQL..." -ForegroundColor Gray
python -c "import sys; sys.path.append('backend'); from database import init_db; init_db()"

Write-Host ""
Write-Host "=========================================================================" -ForegroundColor Green
Write-Host " [OK] SERVIDOR INICIADO EN: http://localhost:5000" -ForegroundColor White
Write-Host " [OK] BASE DE DATOS RELACIONAL: edusmart.db (Transacciones ACID)" -ForegroundColor White
Write-Host " [OK] WHATSAPP OFICIAL: +591 62559281 (Meta Cloud API)" -ForegroundColor White
Write-Host "=========================================================================" -ForegroundColor Green
Write-Host ""

# 4. Abrir navegador
Start-Sleep -Seconds 1
Start-Process "http://localhost:5000"

Write-Host "Servidor en ejecucion. Presiona Ctrl + C para detener." -ForegroundColor DarkGray
Write-Host ""
python backend\app.py
