from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir todas las solicitudes CORS desde cualquier origen

# Base de datos simulada
products = {
    "informales": [
        {"id": 1, "name": "Manzanas", "category": "frutas", "type": "dulces"},
        {"id": 2, "name": "Papas", "category": "Verdura", "type": "variado"},
        {"id": 3, "name": "Fresas", "category": "frutas", "type": "variado"},
        {"id": 4, "name": "Pepinos", "category": "Verdura", "type": "variado"},
        {"id": 5, "name": "Zanahoria", "category": "Verdura", "type": "variado"}
    ],
    "formales": [
        {"id": 1, "name": "Cerveza", "category": "bebidas", "type": "alcoholica"},
        {"id": 2, "name": "Bolso", "category": "accesorios", "type": "ropa"},
        {"id": 3, "name": "Libreta ", "category": "papeleria", "type": "material escolar"},
        {"id": 4, "name": "Telefono", "category": "tecnologia", "type": "dispositivo"},
        {"id": 5, "name": "Reloj", "category": "accesorios", "type": "joyería"}
    ]
}

# Datos del administrador
admin = {
    "id": 1,
    "name": "Admin",
    "email": "admin@example.com"
}

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/admin')
def get_admin():
    return jsonify(admin), 200

@app.route('/products/<vendor_type>', methods=['GET', 'POST'])
def manage_products(vendor_type):
    if vendor_type not in products:
        return jsonify({"error": "Vendor type not found"}), 404

    if request.method == 'GET':
        return jsonify(products[vendor_type]), 200

    if request.method == 'POST':
        new_product = request.json
        if not new_product or not all(k in new_product for k in ("name", "category", "type")):
            return jsonify({"error": "Invalid product data"}), 400
        new_id = len(products[vendor_type]) + 1
        new_product["id"] = new_id
        products[vendor_type].append(new_product)
        return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
