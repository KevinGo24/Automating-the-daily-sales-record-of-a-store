productos = {}
total_general = 0
continuar = "si"

def resumen_ventas():
    global total_general, continuar

    while continuar == "si":
        print('---------  BIENVENIDO A NUESTRO SISTEMA DE VENTAS ------------')
        nombre = input("1 - Ingrese el nombre del producto: ")
        precio = float(input("2 - Ingrese el precio del producto: "))
        if precio <=0 :
            print('Ingrese un precio mayor a 0')
            continue
        cantidad = int(input("3 - Ingrese la cantidad vendida: "))
        if cantidad < 0:
            print('Ingrse una cantidad mayor a 0 ')
            continue


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

        continuar = input("¿Desea registrar otro producto? (si/no): ").lower()

    print("\n--- RESUMEN DE VENTAS DEL DÍA ---")

    for producto, datos in productos.items():
        print("Producto:", producto)
        print("Cantidad total vendida:", datos["cantidad"])
        print("Total por producto:", datos["total"])
        print()

    print("TOTAL GENERAL RECAUDADO:", total_general)


