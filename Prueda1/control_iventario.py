productos = int(input("Ingrese la cantidad de productos a registrar: "))

suma_total_de_todo = 0

while productos > 0:
    nombre_del_producto = str(input("Ingrese el nombre del producto: "))
    precio_del_producto = float(input("Ingrese el precio del producto: "))
    cantidad_del_producto = int(input("Ingrese la cantidad del producto: "))

    if precio_del_producto > 0 and cantidad_del_producto > 0:
        cantidad_total = precio_del_producto * cantidad_del_producto
        print(f"El precio total del producto {nombre_del_producto} es: {cantidad_total}")
        print("Producto registrado correctamente.\n")
        
        suma_total_de_todo = suma_total_de_todo + cantidad_total
    
        productos -= 1    
    else:
        print("El precio y la cantidad deben ser mayores a cero.")
        print("Producto no registrado.")
        print("¿Deseas intentar de nuevo?")
        respuesta = input("Ingrese 'si' para intentar de nuevo o 'no' para salir: ")
        
        if respuesta.lower() == 'si':
            continue
        else:
            print("Gracias por usar el sistema de inventario.")
            break

print("\n" + "="*45)
print(f"EL PRECIO TOTAL DE TODOS LOS PRODUCTOS ES: {suma_total_de_todo}")
print("="*45)
