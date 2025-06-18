#Contexto: Una empresa de ventas quiere desarrollar un sistema básico de gestión de clientes, productos y facturación. 
#El sistema debe permitir el almacenamiento y análisis de datos utilizando estructuras adecuadas. 
#Importante: La carga de datos debe realizarse mediante un menú interactivo que utilice un bucle `while` y 
# solicite al usuario ingresar información. 
#Todos los datos ingresados deben validarse para garantizar que sean correctos antes de agregarlos a las estructuras.
#Objetivo: Crear un programa que permita realizar las siguientes acciones. 
#Para cada punto se indica una sugerencia de implementación.


# sistema_facturacion.py
# Ejercicio integrador - Sistema de Facturación

clientes = []  # Lista que almacena los clientes
productos = []  # Lista que almacena los productos
ventas = []  # Lista que almacena las ventas realizadas

# 1. Cargar un listado de clientes
def agregar_cliente():
    """
    Permite ingresar un nuevo cliente a la lista de clientes.
    Se valida que el ID no se repita y que el nombre y provincia no estén vacíos.
    """
    while True:
        nombre = input("Nombre del cliente: ")
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue

        id_cliente = input("ID del cliente: ")
        if id_cliente == "" or any(c["ID"] == id_cliente for c in clientes):
            print("El ID ya existe o es inválido.")
            continue

        provincia = input("Provincia del cliente: ")
        if provincia == "":
            print("La provincia no puede estar vacía.")
            continue

        clientes.append({"ID": id_cliente, "Nombre": nombre, "Provincia": provincia})
        print("Cliente agregado exitosamente.")
        break

# 2. Cargar un catálogo de productos
def agregar_producto():
    """
    Permite ingresar un nuevo producto al catálogo.
    Se valida que el código no exista previamente y que el precio sea mayor a cero.
    """
    while True:
        codigo = input("Código del producto: ")
        if codigo == "" or any(p["Código"] == codigo for p in productos):
            print("El código ya existe o es inválido.")
            continue

        descripcion = input("Descripción del producto: ")
        if descripcion == "":
            print("La descripción no puede estar vacía.")
            continue

        try:
            precio = float(input("Precio del producto: "))
            if precio <= 0:
                raise ValueError
        except ValueError:
            print("El precio debe ser un número mayor a cero.")
            continue

        productos.append({"Código": codigo, "Descripción": descripcion, "Precio": precio})
        print("Producto agregado exitosamente.")
        break

# 3. Registrar ventas realizadas
def registrar_venta():
    """
    Permite registrar una venta asociada a un cliente.
    Se validan que el cliente exista, que los códigos de producto sean válidos
    y que las cantidades sean mayores a cero.
    """
    if not clientes or not productos:
        print("Debe haber clientes y productos registrados antes de registrar una venta.")
        return
    
    id_cliente = input("Ingrese el ID del cliente: ")
    cliente = next((c for c in clientes if c["ID"] == id_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    fecha = input("Ingrese la fecha de la venta (DD/MM/AAAA): ")
    lista_productos = []

    while True:
        codigo_producto = input("Código del producto (o 'fin' para terminar): ")
        if codigo_producto.lower() == "fin":
            break

        producto = next((p for p in productos if p["Código"] == codigo_producto), None)
        if not producto:
            print("Producto no encontrado.")
            continue

        try:
            cantidad = int(input("Cantidad vendida: "))
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            print("La cantidad debe ser mayor a cero.")
            continue

        lista_productos.append((producto["Código"], cantidad))
    
    ventas.append({"Cliente": id_cliente, "Fecha": fecha, "Productos": lista_productos})
    print("Venta registrada exitosamente.")

# 4. Mostrar el listado completo de clientes y productos
def mostrar_clientes_productos():
    """
    Muestra la lista completa de clientes y productos registrados con un formato legible.
    """
    print("\nClientes registrados:")
    for c in clientes:
        print(f"ID: {c['ID']}, Nombre: {c['Nombre']}, Provincia: {c['Provincia']}")
    
    print("\nProductos registrados:")
    for p in productos:
        print(f"Código: {p['Código']}, Descripción: {p['Descripción']}, Precio: {p['Precio']}")

# 5. Buscar clientes por provincia usando un filtro dinámico
def buscar_clientes_por_provincia():
    """
    Filtra y muestra los clientes que pertenecen a una provincia específica.
    Se usa comprensión de listas para encontrar coincidencias.
    """
    provincia = input("Ingrese la provincia a buscar: ")
    encontrados = [c for c in clientes if c["Provincia"].lower() == provincia.lower()]
    
    if encontrados:
        print(f"\nClientes en {provincia}:")
        for c in encontrados:
            print(f"ID: {c['ID']}, Nombre: {c['Nombre']}")
    else:
        print("No se encontraron clientes en esa provincia.")

# 6. Menú interactivo
def menu():
    """
    Menú principal que permite al usuario interactuar con el sistema de facturación.
    Llama a las funciones de gestión de clientes, productos y ventas.
    """
    while True:
        print("\nMenú Principal:")
        print("1. Agregar cliente")
        print("2. Agregar producto")
        print("3. Registrar venta")
        print("4. Mostrar clientes y productos")
        print("5. Buscar clientes por provincia")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            registrar_venta()
        elif opcion == "4":
            mostrar_clientes_productos()
        elif opcion == "5":
            buscar_clientes_por_provincia()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
