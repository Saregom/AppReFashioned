from flask import Flask, jsonify, request
import refashioned_controller
from db import create_tables

app = Flask(__name__)

#cliente
@app.route('/clientes', methods=["GET"])
def get_clientes():
    clientes = refashioned_controller.get_clientes()
    return jsonify(clientes)


@app.route("/cliente", methods=["POST"])
def insert_cliente():
    detalles_cliente = request.get_json()
    nombre_cliente = detalles_cliente["nombre_cliente"]
    numero_telefonico = detalles_cliente["numero_telefonico"]
    email_cliente = detalles_cliente["email_cliente"]
    usuario = detalles_cliente["usuario"]
    contraseña = detalles_cliente["contraseña"]
    resultado = refashioned_controller.insert_cliente(nombre_cliente, numero_telefonico, email_cliente, usuario, contraseña)
    return jsonify(resultado)


@app.route("/cliente", methods=["PUT"])
def update_cliente():
    detalles_cliente = request.get_json()
    id_cliente = detalles_cliente["id_cliente"]
    nombre_cliente = detalles_cliente["nombre_cliente"]
    numero_telefonico = detalles_cliente["numero_telefonico"]
    email_cliente = detalles_cliente["email_cliente"]
    usuario = detalles_cliente["usuario"]
    contraseña = detalles_cliente["contraseña"]
    resultado = refashioned_controller.update_cliente(id_cliente, nombre_cliente, numero_telefonico, email_cliente, usuario, contraseña)
    return jsonify(resultado)


@app.route("/cliente/<id_cliente>", methods=["DELETE"])
def delete_cliente(id_cliente):
    resultado = refashioned_controller.delete_cliente(id_cliente)
    return jsonify(resultado)


@app.route("/cliente/<id_cliente>", methods=["GET"])
def get_cliente_by_id(id_cliente):
    cliente = refashioned_controller.get_cliente_by_id(id_cliente)
    return jsonify(cliente)

#direcciones

@app.route('/direcciones', methods=["GET"])
def get_direcciones():
    direcciones = refashioned_controller.get_direcciones()
    return jsonify(direcciones)


@app.route("/direccion", methods=["POST"])
def insert_direccion():
    detalles_direccion = request.get_json()
    pais = detalles_direccion["pais"]
    ciudad = detalles_direccion["ciudad"]
    departamento = detalles_direccion["departamento"]
    codigo_postal = detalles_direccion["codigo_postal"]
    direccion = detalles_direccion["direccion"]
    complemento = detalles_direccion["complemento"]
    cliente_id_cliente = detalles_direccion["cliente_id_cliente"]
    resultado = refashioned_controller.insert_direccion(pais, ciudad, departamento, codigo_postal, direccion, complemento, cliente_id_cliente)
    return jsonify(resultado)


@app.route("/direccion", methods=["PUT"])
def update_direccion():
    detalles_direccion = request.get_json()
    id_direccion = detalles_direccion["id_direccion"]
    pais = detalles_direccion["pais"]
    ciudad = detalles_direccion["ciudad"]
    departamento = detalles_direccion["departamento"]
    codigo_postal = detalles_direccion["codigo_postal"]
    direccion = detalles_direccion["direccion"]
    complemento = detalles_direccion["complemento"]
    cliente_id_cliente = detalles_direccion["cliente_id_cliente"]
    resultado = refashioned_controller.update_direccion(id_direccion, pais, ciudad, departamento, codigo_postal, direccion, complemento, cliente_id_cliente)
    return jsonify(resultado)


@app.route("/direccion/<id_direccion>", methods=["DELETE"])
def delete_direccion(id_direccion):
    result = refashioned_controller.delete_direccion(id_direccion)
    return jsonify(result)


@app.route("/direccion/<id_direccion>", methods=["GET"])
def get_direccion_by_id(id_direccion):
    direccion = refashioned_controller.get_direccion_by_id(id_direccion)
    return jsonify(direccion)

#productos
@app.route('/productos', methods=["GET"])
def get_productos():
    productos = refashioned_controller.get_productos()
    return jsonify(productos)


@app.route("/producto", methods=["POST"])
def insert_producto():
    detalles_producto = request.get_json()
    nombre_producto = detalles_producto["nombre_producto"]
    categoria = detalles_producto["categoria"]
    talla = detalles_producto["talla"]
    color = detalles_producto["color"]
    precio = detalles_producto["precio"]
    cantidad_disponible = detalles_producto["cantidad_disponible"]
    resultado = refashioned_controller.insert_producto(nombre_producto, categoria, talla, color, precio, cantidad_disponible)
    return jsonify(resultado)


@app.route("/producto", methods=["PUT"])
def update_producto():
    detalles_producto = request.get_json()
    id_producto = detalles_producto["id_producto"]
    nombre_producto = detalles_producto["nombre_producto"]
    categoria = detalles_producto["categoria"]
    talla = detalles_producto["talla"]
    color = detalles_producto["color"]
    precio = detalles_producto["precio"]
    cantidad_disponible = detalles_producto["cantidad_disponible"]
    resultado = refashioned_controller.update_producto(id_producto, nombre_producto, categoria, talla, color, precio, cantidad_disponible)
    return jsonify(resultado)


@app.route("/producto/<id_producto>", methods=["DELETE"])
def delete_producto(id_producto):
    result = refashioned_controller.delete_producto(id_producto)
    return jsonify(result)


@app.route("/producto/<id_producto>", methods=["GET"])
def get_producto_by_id(id_producto):
    producto = refashioned_controller.get_producto_by_id(id_producto)
    return jsonify(producto)

#envios
@app.route('/envios', methods=["GET"])
def get_envios():
    envios = refashioned_controller.get_envios()
    return jsonify(envios)


@app.route("/envio", methods=["POST"])
def insert_envio():
    detalles_envio = request.get_json()
    fecha_envio = detalles_envio["fecha_envio"]
    estado_envio = detalles_envio["estado_envio"]
    proveedor_envio = detalles_envio["proveedor_envio"]
    direccion_id_direccion = detalles_envio["direccion_id_direccion"]
    direccion_cliente_id_cliente = detalles_envio["direccion_cliente_id_cliente"]
    resultado = refashioned_controller.insert_envio(fecha_envio, estado_envio, proveedor_envio, direccion_id_direccion, direccion_cliente_id_cliente)
    return jsonify(resultado)


@app.route("/envio", methods=["PUT"])
def update_envio():
    detalles_envio = request.get_json()
    id_envio = detalles_envio["id_envio"]
    fecha_envio = detalles_envio["fecha_envio"]
    estado_envio = detalles_envio["estado_envio"]
    proveedor_envio = detalles_envio["proveedor_envio"]
    direccion_id_direccion = detalles_envio["direccion_id_direccion"]
    direccion_cliente_id_cliente = detalles_envio["direccion_cliente_id_cliente"]
    resultado = refashioned_controller.update_envio(id_envio,fecha_envio, estado_envio, proveedor_envio, direccion_id_direccion, direccion_cliente_id_cliente)
    return jsonify(resultado)


@app.route("/envio/<id_envio>", methods=["DELETE"])
def delete_envio(id_envio):
    result = refashioned_controller.delete_envio(id_envio)
    return jsonify(result)


@app.route("/envio/<id_envio>", methods=["GET"])
def get_envio_by_id(id_envio):
    pedido = refashioned_controller.get_envio_by_id(id_envio)
    return jsonify(pedido)

#pedidos
@app.route('/pedidos', methods=["GET"])
def get_pedidos():
    pedidos = refashioned_controller.get_pedidos()
    return jsonify(pedidos)


@app.route("/pedido", methods=["POST"])
def insert_pedido():
    detalles_pedido = request.get_json()
    fecha_pedido = detalles_pedido["fecha_pedido"]
    cliente_id_cliente = detalles_pedido["cliente_id_cliente"]
    envio_id_envio = detalles_pedido["envio_id_envio"]
    resultado = refashioned_controller.insert_pedido(fecha_pedido, cliente_id_cliente, envio_id_envio)
    return jsonify(resultado)


@app.route("/pedido", methods=["PUT"])
def update_pedido():
    detalles_pedido = request.get_json()
    id_pedido = detalles_pedido["id_pedido"]
    fecha_pedido = detalles_pedido["fecha_pedido"]
    cliente_id_cliente = detalles_pedido["cliente_id_cliente"]
    envio_id_envio = detalles_pedido["envio_id_envio"]
    resultado = refashioned_controller.update_pedido(id_pedido, fecha_pedido, cliente_id_cliente, envio_id_envio)
    return jsonify(resultado)


@app.route("/pedido/<id_pedido>", methods=["DELETE"])
def delete_pedido(id_pedido):
    result = refashioned_controller.delete_pedido(id_pedido)
    return jsonify(result)


@app.route("/pedido/<id_pedido>", methods=["GET"])
def get_pedido_by_id(id_pedido):
    pedido = refashioned_controller.get_pedido_by_id(id_pedido)
    return jsonify(pedido)

#Detalles pedidos
@app.route('/detalles_pedidoss', methods=["GET"])
def get_detalles_pedidos():
    detalles_pedidos = refashioned_controller.get_detalles_pedidos()
    return jsonify(detalles_pedidos)


@app.route("/detalles_pedidos", methods=["POST"])
def insert_detalles_pedidos():
    detalles_detalles_pedidos = request.get_json()
    cantidad_ordenada = detalles_detalles_pedidos["cantidad_ordenada"]
    pedido_id_pedido = detalles_detalles_pedidos["pedido_id_pedido"]
    producto_id_producto = detalles_detalles_pedidos["producto_id_producto"]
    resultado = refashioned_controller.insert_detalles_pedidos(cantidad_ordenada, pedido_id_pedido, producto_id_producto)
    return jsonify(resultado)


@app.route("/detalles_pedidos", methods=["PUT"])
def update_detalles_pedidos():
    detalles_detalles_pedidos = request.get_json()
    id_detalles = detalles_detalles_pedidos["id_detalles"]
    cantidad_ordenada = detalles_detalles_pedidos["cantidad_ordenada"]
    pedido_id_pedido = detalles_detalles_pedidos["pedido_id_pedido"]
    producto_id_producto = detalles_detalles_pedidos["producto_id_producto"]
    resultado = refashioned_controller.update_detalles_pedidos(id_detalles, cantidad_ordenada, pedido_id_pedido, producto_id_producto)
    return jsonify(resultado)


@app.route("/detalles_pedidos/<id_detalles>", methods=["DELETE"])
def delete_detalles_pedidos(id_detalles):
    result = refashioned_controller.delete_detalles_pedidos(id_detalles)
    return jsonify(result)


@app.route("/detalles_pedidos/<id_detalles>", methods=["GET"])
def get_detalles_pedidos_by_id(id_detalles):
    detalles_pedidos = refashioned_controller.get_detalles_pedidos_by_id(id_detalles)
    return jsonify(detalles_pedidos)

#facturas
@app.route('/facturas', methods=["GET"])
def get_facturas():
    facturas = refashioned_controller.get_facturas()
    return jsonify(facturas)


@app.route("/factura", methods=["POST"])
def insert_facturas():
    detalles_facturas = request.get_json()
    fecha_emision = detalles_facturas["fecha_emision"]
    metodo_pago = detalles_facturas["metodo_pago"]
    monto_total = detalles_facturas["monto_total"]
    pedido_id_pedido = detalles_facturas["pedido_id_pedido"]
    cliente_id_cliente =detalles_facturas["cliente_id_cliente"]
    resultado = refashioned_controller.insert_factura(fecha_emision, metodo_pago, monto_total, pedido_id_pedido, cliente_id_cliente)
    return jsonify(resultado)


@app.route("/factura", methods=["PUT"])
def update_factura():
    detalles_facturas = request.get_json()
    id_factura = detalles_facturas["id_factura"]
    fecha_emision = detalles_facturas["fecha_emision"]
    metodo_pago = detalles_facturas["metodo_pago"]
    monto_total = detalles_facturas["monto_total"]
    pedido_id_pedido = detalles_facturas["pedido_id_pedido"]
    cliente_id_cliente =detalles_facturas["cliente_id_cliente"]
    resultado = refashioned_controller.update_factura(id_factura, fecha_emision, metodo_pago, monto_total, pedido_id_pedido, cliente_id_cliente)
    return jsonify(resultado)


@app.route("/factura/<id_factura>", methods=["DELETE"])
def delete_factura(id_factura):
    result = refashioned_controller.delete_factura(id_factura)
    return jsonify(result)


@app.route("/factura/<id_factura>", methods=["GET"])
def get_factura_by_id(id_factura):
    factura = refashioned_controller.get_factura_by_id(id_factura)
    return jsonify(factura)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
