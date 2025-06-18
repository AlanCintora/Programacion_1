#A.Contexto
#Una empresa de ventas desea desarrollar un sistema básico de gestión
#de clientes, productos y facturación.
#El sistema debe permitir almacenar los datos en archivos y utilizar estructuras de datos 
#apropiadas para su análisis y consulta.


import json
import os

# Nombre de archivos
CLIENTES_FILE = "clientes.json"
PRODUCTOS_FILE = "productos.json"
VENTAS_FILE = "ventas.json"

def leer_archivo(nombre_archivo):
    """
    Lee el contenido de un archivo JSON.
    Si el archivo no existe, devuelve una lista vacía.
    """
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

def escribir_archivo(nombre_archivo, datos):
    """
    Guarda datos en un archivo JSON.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

# Cargar clientes con validaciones
def agregar_cliente():
    """
    Agrega un nuevo cliente validando que el ID sea único y que los campos no estén vacíos.
    Guarda el cliente en el archivo JSON.
    """
    clientes = leer_archivo(CLIENTES_FILE)

    nombre = input("Ingrese el nombre del cliente: ").strip()
    id_cliente = input("Ingrese el ID del cliente: ").strip()
    provincia = input("Ingrese la provincia del cliente: ").strip()

    if not nombre or not id_cliente or not provincia:
        print("Error: Todos los campos son obligatorios.")
        return
    
    if any(cliente["id"] == id_cliente for cliente in clientes):
        print("Error: El ID ya existe en el sistema.")
        return

    cliente = {"id": id_cliente, "nombre": nombre, "provincia": provincia}
    clientes.append(cliente)
    escribir_archivo(CLIENTES_FILE, clientes)
    print("Cliente agregado correctamente.")

# Cargar productos con validaciones
def agregar_producto():
    """
    Registra un nuevo producto validando código único y precio mayor a 0.
    Guarda el producto en el archivo JSON.
    """
    productos = leer_archivo(PRODUCTOS_FILE)

    codigo = input("Ingrese el código del producto: ").strip()
    descripcion = input("Ingrese la descripción del producto: ").strip()
    
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            raise ValueError
    except ValueError:
        print("Error: El precio debe ser un número mayor a cero.")
        return
    
    if any(producto["codigo"] == codigo for producto in productos):
        print("Error: El código del producto ya existe.")
        return

    producto = {"codigo": codigo, "descripcion": descripcion, "precio": precio}
    productos.append(producto)
    escribir_archivo(PRODUCTOS_FILE, productos)
    print("Producto agregado correctamente.")
