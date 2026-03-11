
productos = int(input("¿Cuanta compra va a realizar ? "))
def registrar_ventas():
    
    for i in range(productos):
        print(f"\n--- Registro del Producto #{i + 1} ---")
        # Pedimos los 3 datos necesarios
        nombre = input("Nombre del producto: ")
        precio = int(input(f"Precio unitario de {nombre}: "))
        cantidad = int(input("Cantidad de unidades vendidas: "))
        
        # Aquí iría tu lógica para guardar o calcular
        subtotal = precio * cantidad
        print(f"Subtotal de esta venta: ${subtotal}")
        
        