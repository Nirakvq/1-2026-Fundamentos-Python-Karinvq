saldo = 0.0

saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
if saldo_inicial >= 0:
    saldo = saldo_inicial
else:
    print("Saldo inválido. Se iniciará con 0.0")

def consultar_saldo():
    print(f"\nTu saldo actual es: ₡{saldo}")

def depositar():
    global saldo
    monto = float(input("\nIngresa el monto que deseas depositar: "))
    if monto > 0:
        saldo = saldo + monto
        print(f"¡Depósito exitoso! Has depositado: ₡{monto}")
        print(f"Tu nuevo saldo es: ₡{saldo}")
    else:
        print("El monto debe ser mayor a cero.")

def retirar():
    global saldo
    monto = float(input("\nIngresa el monto que deseas retirar: "))
    if monto > saldo:
        print("Error: No tienes suficiente saldo para este retiro.")
    elif monto <= 0:
        print("El monto debe ser mayor a cero.")
    else:
        saldo = saldo - monto
        print(f"¡Retiro exitoso! Has retirado: ₡{monto}")
        print(f"Tu nuevo saldo es: ₡{saldo}")

continuar = True

while continuar:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        consultar_saldo()
    elif opcion == "2":
        depositar()
    elif opcion == "3":
        retirar()
    elif opcion == "4":
        print("\nGracias por usar el cajero automático. ¡Hasta luego!")
        continuar = False
    else:
        print("Opción inválida. Por favor, elige un número del 1 al 4.")
