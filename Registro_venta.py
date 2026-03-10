import Solicitar_usuario fro

for i in range(cantidad_productos):
    print(f"\n--- Registro del Producto #{i + 1} ---")
    
    # Pedimos los 3 datos necesarios
    nombre = input("Nombre del producto: ")
    precio = float(input(f"Precio unitario de {nombre}: "))
    cantidad = int(input(f"Cantidad de unidades vendidas: "))
    
    # Aquí iría tu lógica para guardar o calcular
    subtotal = precio * cantidad
    print(f"Subtotal de esta venta: ${subtotal}")