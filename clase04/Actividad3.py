print("cajero automático")
print("Bienvenido al cajero autompático")
saldo = 0

while True:
    print("1. consultar saldo")
    print("2. retirar dinero")
    print("3. depositar dinero")
    print("4. salir")
    opcion = int(input("seleccione una opcipón:"))
    if opcion == 1:
        print(f"su saldo es: {saldo}")
    elif opcion == 2:
        cantidad = int(input("ingrese la cantidad a retirar:"))
        if cantidad > saldo:
            print("no tiene suficiente saldo")
        else:
            saldo = saldo - cantidad
            print(f"Ha retirado : {cantidad}")
    elif opcion == 3:
        cantidad = int(input("ingrese la cantidad a depositar:"))
        saldo = saldo + cantidad
        print(f"Ha depositado : {cantidad}")
    elif opcion == 4:
            print("gracias por usar el cajero automático")
            break
    else:
        print("opción no válida")



    