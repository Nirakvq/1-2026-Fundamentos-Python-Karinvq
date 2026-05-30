productos = int(input("Ingrese la cantidad de productos a registrar: "))
while productos >0:
     nombre_del_producto = (input("Ingrese el nombre del producto: "))
     precio_del_producto = float(input("Ingrese el precio del producto: "))
     cantidad_del_producto = int(input("Ingrese la cantidad del producto: "))
     if precio_del_producto > 0 and cantidad_del_producto > 0:
        print("Producto registrado correctamente")
     else:
        print("El precio y la cantidad deben ser mayores a 0")
        print("Producto no registrado")
        print("Deseas intentar de nuevo?")
        respuesta = input("Ingrese 'si' para intentar de nuevo o 'no' para salir: ")
     if respuesta.lower() == 'si':
        continue
     else:
         print("Gracias por usar el sistema de inventario")
         break   