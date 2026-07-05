from flask import Flask, render_template, request

app = Flask(__name__)

# Catálogo de Laptops
laptops = [
    {"id": 1, "nombre": "Notebook Pro", "precio": 800, "stock": 5},
    {"id": 2, "nombre": "Laptop Gamer", "precio": 1200, "stock": 3}
]

# Flujo de estados (Paso 5 al 9 de tu imagen)
estado_pedido = "Recibido"

@app.route('/')
def index():
    return render_template('index.html', productos=laptops)

@app.route('/comprar', methods=['POST'])
def comprar():
    global estado_pedido
    producto_id = int(request.form.get('id'))
    # Lógica de reducción de inventario
    for p in laptops:
        if p['id'] == producto_id and p['stock'] > 0:
            p['stock'] -= 1
            estado_pedido = "En preparación"
            return f"Compra exitosa. Estado actual: {estado_pedido}"
    return "Error: Sin stock"

if __name__ == '__main__':
    app.run(debug=True)
  
