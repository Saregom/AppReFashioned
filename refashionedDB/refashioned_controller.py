from db import get_db

#cliente
def insert_cliente(nombre_cliente, numero_telefonico, email_cliente, usuario, contraseña):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO clientes(nombre_cliente, numero_telefonico, email_cliente, usuario, contraseña) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [nombre_cliente, numero_telefonico, email_cliente, usuario, contraseña])
    db.commit()
    return True


def update_cliente(id_cliente, nombre_cliente, numero_telefonico, email_cliente, usuario, contraseña):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE clientes SET nombre_cliente = ?, numero_telefonico = ?, email_cliente = ?, usuario = ?, contraseña = ? WHERE id_cliente = ?"
    cursor.execute(statement, [nombre_cliente, numero_telefonico, email_cliente, usuario, contraseña, id_cliente])
    db.commit()
    return True


def delete_cliente(id_cliente):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM clientes WHERE id_cliente = ?"
    cursor.execute(statement, [id_cliente])
    db.commit()
    return True


def get_cliente_by_id(id_cliente):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id_cliente, nombre_cliente, numero_telefonico, email_cliente, usuario, contraseña FROM clientes WHERE id_cliente = ?"
    cursor.execute(statement, [id_cliente])
    return cursor.fetchone()


def get_clientes():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_cliente, nombre_cliente, numero_telefonico, email_cliente, usuario, contraseña FROM clientes"
    cursor.execute(query)
    return cursor.fetchall()

#direccion
def insert_direccion(pais, ciudad, departamento, codigo_postal, direccion, complemento, cliente_id_cliente):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO direcciones(pais, ciudad, departamento, codigo_postal, direccion, complemento, cliente_id_cliente) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [pais, ciudad, departamento, codigo_postal, direccion, complemento, cliente_id_cliente])
    db.commit()
    return True


def update_direccion(id_direccion, pais, ciudad, departamento, codigo_postal, direccion, complemento, cliente_id_cliente):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE direcciones SET pais = ?, ciudad = ?, departamento = ?, codigo_postal = ?, direccion = ?, complemento = ?, cliente_id_cliente = ? WHERE id_direccion = ?"
    cursor.execute(statement, [pais, ciudad, departamento, codigo_postal, direccion, complemento, cliente_id_cliente, id_direccion])
    db.commit()
    return True


def delete_direccion(id_direccion):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM direcciones WHERE id_direccion = ?"
    cursor.execute(statement, [id_direccion])
    db.commit()
    return True


def get_direccion_by_id(id_direccion):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT pais, ciudad, departamento, codigo_postal, direccion, complemento, cliente_id_cliente FROM direcciones WHERE id_direccion = ?"
    cursor.execute(statement, [id_direccion])
    return cursor.fetchone()


def get_direcciones():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_direccion, pais, ciudad, departamento, codigo_postal, direccion, complemento, cliente_id_cliente FROM direcciones"
    cursor.execute(query)
    return cursor.fetchall()

#productos
def insert_producto(nombre_producto, categoria, talla, color, precio, cantidad_disponible):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO productos(nombre_producto, categoria, talla, color, precio, cantidad_disponible) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [nombre_producto, categoria, talla, color, precio, cantidad_disponible])
    db.commit()
    return True


def update_producto(id_producto, nombre_producto, categoria, talla, color, precio, cantidad_disponible):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE productos SET nombre_producto = ?, categoria = ?, talla = ?, color = ?, precio = ?, cantidad_disponible = ? WHERE id_producto = ?"
    cursor.execute(statement, [nombre_producto, categoria, talla, color, precio, cantidad_disponible, id_producto])
    db.commit()
    return True


def delete_producto(id_producto):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM productos WHERE id_producto = ?"
    cursor.execute(statement, [id_producto])
    db.commit()
    return True


def get_producto_by_id(id_producto):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id_producto, nombre_producto, categoria, talla, color, precio, cantidad_disponible FROM productos WHERE id_producto = ?"
    cursor.execute(statement, [id_producto])
    return cursor.fetchone()


def get_productos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_producto, nombre_producto, categoria, talla, color, precio, cantidad_disponible FROM productos"
    cursor.execute(query)
    return cursor.fetchall()

#envios
def insert_envio(fecha_envio, estado_envio, proveedor_envio, direccion_id_direccion, direccion_cliente_id_cliente):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO envios(fecha_envio, estado_envio, proveedor_envio, direccion_id_direccion, direccion_cliente_id_cliente) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [fecha_envio, estado_envio, proveedor_envio, direccion_id_direccion, direccion_cliente_id_cliente])
    db.commit()
    return True


def update_envio(id_envio, fecha_envio, estado_envio, proveedor_envio, direccion_id_direccion, direccion_cliente_id_cliente):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE envios SET fecha_envio = ?, estado_envio = ?, proveedor_envio = ?, direccion_id_direccion = ?, direccion_cliente_id_cliente = ? WHERE id_envio = ?"
    cursor.execute(statement, [fecha_envio, estado_envio, proveedor_envio, direccion_id_direccion, direccion_cliente_id_cliente, id_envio])
    db.commit()
    return True


def delete_envio(id_envio):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM envios WHERE id_envio = ?"
    cursor.execute(statement, [id_envio])
    db.commit()
    return True


def get_envio_by_id(id_envio):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id_envio, fecha_envio, estado_envio, proveedor_envio, direccion_id_direccion, direccion_cliente_id_cliente FROM envios WHERE id_envio = ?"
    cursor.execute(statement, [id_envio])
    return cursor.fetchone()


def get_envios():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_envio, fecha_envio, estado_envio, proveedor_envio, direccion_id_direccion, direccion_cliente_id_cliente FROM envios"
    cursor.execute(query)
    return cursor.fetchall()

#pedidos
def insert_pedido(fecha_pedido, cliente_id_cliente, envio_id_envio):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO pedidos(fecha_pedido, cliente_id_cliente, envio_id_envio) VALUES (?, ?, ?)"
    cursor.execute(statement, [fecha_pedido, cliente_id_cliente, envio_id_envio])
    db.commit()
    return True


def update_pedido(id_pedido, fecha_pedido, cliente_id_cliente, envio_id_envio):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE pedidos SET fecha_pedido = ?, cliente_id_cliente = ?, envio_id_envio = ? WHERE id_pedido = ?"
    cursor.execute(statement, [fecha_pedido, cliente_id_cliente, envio_id_envio, id_pedido ])
    db.commit()
    return True


def delete_pedido(id_pedido):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM pedidos WHERE id_pedido = ?"
    cursor.execute(statement, [id_pedido])
    db.commit()
    return True


def get_pedido_by_id(id_pedido):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id_pedido, fecha_pedido, cliente_id_cliente, envio_id_envio FROM pedidos WHERE id_pedido = ?"
    cursor.execute(statement, [id_pedido])
    return cursor.fetchone()


def get_pedidos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_pedido, fecha_pedido, cliente_id_cliente, envio_id_envio FROM pedidos"
    cursor.execute(query)
    return cursor.fetchall()

#detalles pedidos
def insert_detalles_pedidos(cantidad_ordenada, pedido_id_pedido, producto_id_producto):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO detalles_pedidos(cantidad_ordenada, pedido_id_pedido, producto_id_producto) VALUES (?, ?, ?)"
    cursor.execute(statement, [cantidad_ordenada, pedido_id_pedido, producto_id_producto])
    db.commit()
    return True


def update_detalles_pedidos(id_detalles, cantidad_ordenada, pedido_id_pedido, producto_id_producto):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE detalles_pedidos SET cantidad_ordenada = ?, pedido_id_pedido = ?, producto_id_producto = ? WHERE id_detalles = ?"
    cursor.execute(statement, [cantidad_ordenada, pedido_id_pedido, producto_id_producto, id_detalles ])
    db.commit()
    return True


def delete_detalles_pedidos(id_detalles):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM detalles_pedidos WHERE id_detalles = ?"
    cursor.execute(statement, [id_detalles])
    db.commit()
    return True


def get_detalles_pedidos_by_id(id_detalles):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id_detalles, cantidad_ordenada, pedido_id_pedido, producto_id_producto FROM detalles_pedidos WHERE id_detalles = ?"
    cursor.execute(statement, [id_detalles])
    return cursor.fetchone()


def get_detalles_pedidos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_detalles, cantidad_ordenada, pedido_id_pedido, producto_id_producto FROM detalles_pedidos"
    cursor.execute(query)
    return cursor.fetchall()

#facturas

def insert_factura(fecha_emision, metodo_pago, monto_total, pedido_id_pedido, cliente_id_cliente):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO facturas(fecha_emision, metodo_pago, monto_total, pedido_id_pedido, cliente_id_cliente) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [fecha_emision, metodo_pago, monto_total, pedido_id_pedido, cliente_id_cliente])
    db.commit()
    return True


def update_factura(id_factura, fecha_emision, metodo_pago, monto_total, pedido_id_pedido, cliente_id_cliente):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE facturas SET fecha_emision = ?, metodo_pago = ?, monto_total = ?, pedido_id_pedido = ?, cliente_id_cliente = ? WHERE id_factura = ?"
    cursor.execute(statement, [fecha_emision, metodo_pago, monto_total, pedido_id_pedido, cliente_id_cliente, id_factura])
    db.commit()
    return True


def delete_factura(id_factura):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM facturas WHERE id_factura = ?"
    cursor.execute(statement, [id_factura])
    db.commit()
    return True


def get_factura_by_id(id_factura):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id_factura, fecha_emision, metodo_pago, monto_total, pedido_id_pedido, cliente_id_cliente FROM facturas WHERE id_factura = ?"
    cursor.execute(statement, [id_factura])
    return cursor.fetchone()


def get_facturas():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_factura, fecha_emision, metodo_pago, monto_total, pedido_id_pedido, cliente_id_cliente FROM facturas"
    cursor.execute(query)
    return cursor.fetchall()