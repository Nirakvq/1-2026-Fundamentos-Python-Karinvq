class Vehículos:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_vehiculos(self):
        for vehículo in self.vehiculos:
            print(f"{vehículo.marca} {vehículo.modelo} ({vehículo.año})")

ingresar_vehiculos = int(input("Ingrese la cantidad de vehículos a registrar: "))

cantidad_total_de_vehiculos = 0

while ingresar_vehiculos > 0:
    marca_del_vehiculo = str(input("Ingrese la marca del vehículo: "))
    modelo_del_vehiculo = str(input("Ingrese el modelo del vehículo: "))
    año_del_vehiculo = int(input("Ingrese el año del vehículo: "))

    print(f"Vehículo registrado: {marca_del_vehiculo} {modelo_del_vehiculo} ({año_del_vehiculo})")
    ingresar_vehiculos -= 1