productos = {}
total_general = 0
continuar = "si"

def resumen_ventas():
    global total_general, continuar

    while continuar == "si":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad vendida: "))
        precio = float(input("Ingrese el precio del producto: "))

        total_producto = cantidad * precio
        total_general += total_producto

        if nombre in productos:
            productos[nombre]["cantidad"] += cantidad
            productos[nombre]["total"] += total_producto
        else:
            productos[nombre] = {
                "cantidad": cantidad,
                "total": total_producto
            }

        continuar = input("¿Desea registrar otro producto? (si/no): ")

    print("\n--- RESUMEN DE VENTAS DEL DÍA ---")

    for producto, datos in productos.items():
        print("Producto:", producto)
        print("Cantidad total vendida:", datos["cantidad"])
        print("Total por producto:", datos["total"])
        print()

    print("TOTAL GENERAL RECAUDADO:", total_general)


resumen_ventas()