"""
Test suite for EduSmart Python Backend & SQL Database
"""
import sys
from app import app
import json

def test_api():
    client = app.test_client()

    print("\n--- 1. Testing GET /api/status ---")
    res = client.get('/api/status')
    assert res.status_code == 200
    data = res.get_json()
    print("Status response:", data['motor_bd'], "| Products:", data['metricas']['productos_en_inventario'])

    print("\n--- 2. Testing GET /api/productos ---")
    res = client.get('/api/productos')
    assert res.status_code == 200
    prods = res.get_json()['data']
    print(f"Retrieved {len(prods)} products from SQL database.")
    sample = prods[0]
    print(f"Sample product: {sample['name']} | Initial Stock: {sample['stock']}")

    initial_stock = sample['stock']
    prod_id = sample['id']

    print("\n--- 3. Testing POST /api/ventas (Transaction + Stock Discount) ---")
    order_payload = {
        "customerName": "Test Estudiante",
        "customerPhone": "Opción no disponible todavía",
        "customerEmail": "test@colegio.edu",
        "customerAddress": "Aula 3B",
        "paymentMethod": "QR / Transferencia",
        "items": [
            {"id": prod_id, "name": sample['name'], "price": sample['price'], "quantity": 2}
        ]
    }
    res = client.post('/api/ventas', data=json.dumps(order_payload), content_type='application/json')
    assert res.status_code == 201
    order_data = res.get_json()
    print("Order created:", order_data['orden']['id'], "| Total:", order_data['orden']['total'])
    print("WhatsApp webhook dispatched to:", order_data['meta_cloud_webhook']['recipient_phone'])

    # Verify stock reduction in database
    res_prod = client.get(f'/api/productos/{prod_id}')
    updated_stock = res_prod.get_json()['data']['stock']
    print(f"Stock before: {initial_stock} -> Stock after sale: {updated_stock}")
    assert updated_stock == initial_stock - 2, "Stock was not decremented properly!"
    print("[PASS] Automatic stock discount verified in real SQL database!")

    print("\n--- 4. Testing GET /api/reportes/semanal-pdf ---")
    res_pdf = client.get('/api/reportes/semanal-pdf')
    assert res_pdf.status_code == 200
    assert len(res_pdf.data) > 1000
    print(f"PDF successfully generated with size: {len(res_pdf.data)} bytes")

    print("\n==========================================")
    print(" ALL BACKEND TESTS PASSED SUCCESSFULLY! ")
    print("==========================================")

if __name__ == '__main__':
    test_api()
