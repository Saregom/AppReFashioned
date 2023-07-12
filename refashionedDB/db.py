import sqlite3
DATABASE_NAME = "refashioned.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS clientes(
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_cliente TEXT NOT NULL,
        numero_telefonico INTEGER NOT NULL,
        email_cliente TEXT NOT NULL,
        usuario TEXT NOT NULL,
        contraseña TEXT NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS direcciones(
        id_direccion INTEGER PRIMARY KEY AUTOINCREMENT,
        pais TEXT NOT NULL,
        ciudad TEXT NOT NULL,
        departamento TEXT NOT NULL,
        codigo_postal INTEGER NOT NULL,
        direccion TEXT NOT NULL,
        complemento TEXT NOT NULL,
        cliente_id_cliente INTEGER NOT NULL,
        FOREIGN KEY(cliente_id_cliente) REFERENCES clientes(id_cliente)
        )""",
        """CREATE TABLE IF NOT EXISTS productos(
        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL,
        categoria TEXT NOT NULL,
        talla TEXT NOT NULL,
        color TEXT NOT NULL,
        precio INTEGER NOT NULL,
        cantidad_disponible INTEGER NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS envios(
        id_envio INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_envio TEXT NOT NULL,
        estado_envio TEXT NOT NULL,
        proveedor_envio TEXT NOT NULL,
        direccion_id_direccion INTEGER NOT NULL,
        direccion_cliente_id_cliente INTEGER NOT NULL,
        FOREIGN KEY(direccion_id_direccion) REFERENCES direcciones(id_direccion),
        FOREIGN KEY(direccion_cliente_id_cliente) REFERENCES direcciones(cliente_id_cliente)
        )""",
        """CREATE TABLE IF NOT EXISTS pedidos(
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_pedido TEXT NOT NULL,
        cliente_id_cliente INTEGER NOT NULL,
        envio_id_envio INTEGER NOT NULL,
        FOREIGN KEY(cliente_id_cliente) REFERENCES clientes(id_cliente),
        FOREIGN KEY(envio_id_envio) REFERENCES envios(id_envio)
        )""",
        """CREATE TABLE IF NOT EXISTS detalles_pedidos(
        id_detalles INTEGER PRIMARY KEY AUTOINCREMENT,
        cantidad_ordenada INTEGER NOT NULL,
        pedido_id_pedido INTEGER NOT NULL,
        producto_id_producto INTEGER NOT NULL,
        FOREIGN KEY(pedido_id_pedido) REFERENCES pedidos(id_pedido),
        FOREIGN KEY(producto_id_producto) REFERENCES productos(id_producto)
        )""",
        """CREATE TABLE IF NOT EXISTS facturas(
        id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_emision TEXT NOT NULL,
        metodo_pago TEXT NOT NULL,
        monto_total INTEGER NOT NULL,
        pedido_id_pedido INTEGER NOT NULL,
        cliente_id_cliente INTEGER NOT NULL,
        FOREIGN KEY(pedido_id_pedido) REFERENCES pedidos(id_pedido),
        FOREIGN KEY(cliente_id_cliente) REFERENCES clientes(id_cliente)
        )"""    
        ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
