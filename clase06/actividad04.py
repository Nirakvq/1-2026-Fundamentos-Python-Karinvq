
while True:
    print("1. registrar estudiantes")
    print("2. ver todos los estudiantes registrados")
    print("3. salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        archivo = open(r"C:\Users\La Cometa\Desktop\1-2026-Fundamentos-Python-Karinvq\clase05\actividad.txt", "a")
        print("Registrar estudiantes")
        nombre = str(input("Ingrese el nombre del estudiante: "))
        carnet = str(input("Ingrese el carnet del estudiante: "))
        nota = float(input("Ingrese la nota del estudiante: "))

        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Carnet: {carnet}\n")
        archivo.write(f"Nota: {nota}\n")
        archivo.close()
    
    elif opcion == 2:
        archivo = open(r"C:\Users\La Cometa\Desktop\1-2026-Fundamentos-Python-Karinvq\clase05\actividad.txt", "r")
        print("Ver todos los estudiantes registrados")
        estudiantes = archivo.read()
        print(estudiantes)
        archivo.close()
    elif opcion == 3:
        print("Salir")
        break
