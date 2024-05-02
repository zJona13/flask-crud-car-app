from bd import obtener_conexion


def descuento_precio(precio):
    descuento = None
    
    if(precio >= 20000 ): 
        descuento = precio * 0.05
    else:
        descuento = precio * 0.03
    return descuento


def insertar_carros(marca, modelo, color, precio, cuotas):
    conexion = obtener_conexion()
    descuento = descuento_precio(precio)
    interes = 0.10
    precio_cuota = (precio * interes) / cuotas

    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO carros(marca, modelo, color, precio, cuotas, descuento, precio_cuota) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (marca, modelo, color, precio, cuotas, descuento, precio_cuota))
    conexion.commit()
    conexion.close()


def obtener_carros():
    conexion = obtener_conexion()
    carros=[]
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM carros")
        carros = cursor.fetchall()
    conexion.close()
    return carros


def eliminar_carros(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM carros WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_carros_por_id(id):
    conexion = obtener_conexion()
    carro = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM carros WHERE id = %s", (id,))
        carro = cursor.fetchone()
    conexion.close()
    return carro


def actualizar_carros(marca, modelo, color, precio, cuotas, id):
    conexion = obtener_conexion()
    descuento = descuento_precio(precio)
    interes = 0.10
    precio_cuota = (precio * interes) / cuotas

    with conexion.cursor() as cursor:
        cursor.execute("UPDATE carros SET marca = %s, modelo = %s, color = %s, precio = %s, cuotas = %s, descuento = %s, precio_cuota = %s WHERE id = %s",
                       (marca, modelo, color, precio, cuotas, descuento, precio_cuota, id))
    conexion.commit()
    conexion.close()