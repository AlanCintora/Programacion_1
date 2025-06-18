import funciones_JSON
from datetime import datetime
import os

# Nombres de archivos para la persistencia de datos
CLIENTES_FILE = "clientes.json"
PRODUCTOS_FILE = "productos.json"
VENTAS_FILE = "ventas.json"

def registrar_venta():
    """
    Registra una nueva venta en el sistema.
    - Valida que el cliente exista y que los productos sean válidos.
    - Almacena la venta en el archivo JSON con fecha y productos comprados.
    """
    clientes = funciones_JSON.leer_archivo(CLIENTES_FILE)
    productos = funciones_JSON.leer_archivo(PRODUCTOS_FILE)
    ventas = funciones_JSON.leer_archivo(VENTAS_FILE)

    if not clientes or not productos:
        print("Debe haber clientes y productos registrados antes de registrar una venta.")
        return

    id_cliente = input("Ingrese el ID del cliente: ").strip()
    cliente = next((c for c in clientes if c["id"] == id_cliente), None)
    if not cliente:
        print("Error: Cliente no encontrado.")
        return

    fecha = datetime.now().strftime("%d/%m/%Y")
    lista_productos = []

    while True:
        codigo_producto = input("Código del producto (o 'fin' para terminar): ").strip()
        if codigo_producto.lower() == "fin":
            break

        producto = next((p for p in productos if p["codigo"] == codigo_producto), None)
        if not producto:
            print("Error: Producto no encontrado.")
            continue

        try:
            cantidad = int(input("Cantidad vendida: "))
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            print("Error: La cantidad debe ser mayor a cero.")
            continue

        lista_productos.append((codigo_producto, cantidad))

    if lista_productos:
        venta = {"Cliente": id_cliente, "Fecha": fecha, "Productos": lista_productos}
        ventas.append(venta)
        funciones_JSON.escribir_archivo(VENTAS_FILE, ventas)
        print("Venta registrada exitosamente.")

def mostrar_clientes_productos():
    """
    Muestra la lista completa de clientes y productos registrados.
    - Lee los datos de los archivos JSON.
    - Imprime la información en pantalla con formato legible.
    """
    clientes = funciones_JSON.leer_archivo(CLIENTES_FILE)
    productos = funciones_JSON.leer_archivo(PRODUCTOS_FILE)

    print("\nClientes registrados:")
    for c in clientes:
        print(f"ID: {c['id']}, Nombre: {c['nombre']}, Provincia: {c['provincia']}")

    print("\nProductos registrados:")
    for p in productos:
        print(f"Código: {p['codigo']}, Descripción: {p['descripcion']}, Precio: {p['precio']}")

def buscar_clientes_por_provincia():
    """
    Filtra y muestra los clientes que pertenecen a una provincia específica.
    - Utiliza comprensión de listas para obtener los clientes coincidentes.
    """
    clientes = funciones_JSON.leer_archivo(CLIENTES_FILE)
    provincia = input("Ingrese la provincia a buscar: ").strip().lower()

    encontrados = [c for c in clientes if c["provincia"].lower() == provincia]

    if encontrados:
        print(f"\nClientes en {provincia.capitalize()}:")
        for c in encontrados:
            print(f"ID: {c['id']}, Nombre: {c['nombre']}")
    else:
        print("No se encontraron clientes en esa provincia.")

def mostrar_detalle_ventas():
    """
    Muestra el detalle de todas las ventas registradas.
    - Cruza información con el catálogo de productos para calcular subtotales y totales por factura.
    """
    clientes = funciones_JSON.leer_archivo(CLIENTES_FILE)
    productos = funciones_JSON.leer_archivo(PRODUCTOS_FILE)
    ventas = funciones_JSON.leer_archivo(VENTAS_FILE)

    if not ventas:
        print("No hay ventas registradas.")
        return

    for venta in ventas:
        cliente = next((c for c in clientes if c["id"] == venta["Cliente"]), {})
        print(f"\nFactura - Cliente: {cliente.get('nombre', 'Desconocido')} ({venta['Cliente']}) - Fecha: {venta['Fecha']}")

        total_factura = 0
        for codigo_producto, cantidad in venta["Productos"]:
            producto = next((p for p in productos if p["codigo"] == codigo_producto), {})
            subtotal = producto.get("precio", 0) * cantidad
            total_factura += subtotal
            print(f"Producto: {producto.get('descripcion', 'Desconocido')} - Cantidad: {cantidad} - Subtotal: ${subtotal:.2f}")

        print(f"Total factura: ${total_factura:.2f}")

def eliminar_producto():
    """
    Permite eliminar un producto siempre que no se encuentre en una venta.
    - Comprueba si el producto ha sido registrado en alguna venta antes de eliminarlo.
    """
    productos = funciones_JSON.leer_archivo(PRODUCTOS_FILE)
    ventas = funciones_JSON.leer_archivo(VENTAS_FILE)

    productos_vendidos = {codigo_producto for venta in ventas for codigo_producto, _ in venta["Productos"]}

    codigo_eliminar = input("Ingrese el código del producto a eliminar: ").strip()

    if codigo_eliminar in productos_vendidos:
        print("Error: No se puede eliminar un producto que ha sido vendido.")
        return

    productos = [p for p in productos if p["codigo"] != codigo_eliminar]
    funciones_JSON.escribir_archivo(PRODUCTOS_FILE, productos)
    print("Producto eliminado correctamente.")

def eliminar_cliente():
    """
    Permite eliminar un cliente si no ha realizado ninguna compra.
    - Comprueba si el cliente tiene ventas antes de eliminarlo.
    """
    clientes = funciones_JSON.leer_archivo(CLIENTES_FILE)
    ventas = funciones_JSON.leer_archivo(VENTAS_FILE)

    clientes_con_ventas = {venta["Cliente"] for venta in ventas}

    id_eliminar = input("Ingrese el ID del cliente a eliminar: ").strip()

    if id_eliminar in clientes_con_ventas:
        print("Error: No se puede eliminar un cliente con ventas registradas.")
        return

    clientes = [c for c in clientes if c["id"] != id_eliminar]
    funciones_JSON.escribir_archivo(CLIENTES_FILE, clientes)
    print("Cliente eliminado correctamente.")

def menu():
    """
    Menú principal del sistema de facturación.
    - Permite gestionar clientes, productos y ventas.
    - Ejecuta cada acción según la opción seleccionada.
    """
    while True:
        print("\nMenú Principal:")
        print("1. Registrar venta")
        print("2. Mostrar clientes y productos")
        print("3. Buscar clientes por provincia")
        print("4. Mostrar detalle de ventas")
        print("5. Eliminar producto")
        print("6. Eliminar cliente")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_clientes_productos()
        elif opcion == "3":
            buscar_clientes_por_provincia()
        elif opcion == "4":
            mostrar_detalle_ventas()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            eliminar_cliente()
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
