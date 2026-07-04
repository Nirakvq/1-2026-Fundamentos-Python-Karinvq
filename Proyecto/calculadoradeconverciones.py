from colorama import init, Fore

init()

class Calculadora:

    def __init__(self, celcius=None, fahrenheit=None):
        self.celcius = celcius
        self.fahrenheit = fahrenheit

    def convertir_celcius_a_fahrenheit(self):
        return (self.celcius * 9/5) + 32

    def convertir_fahrenheit_a_celcius(self):
        return (self.fahrenheit - 32) * 5/9
    
    def convertir_longitud(self, valor, factor):
        return valor * factor

def main():
    calculadora = Calculadora()
    print("Bienvenido al convertidor de unidades")

    while True:
        
        print(Fore.LIGHTBLUE_EX + "1. Temperatura")
        print(Fore.MAGENTA + "2. Longitud")
        print(Fore.GREEN + "3. Salir")
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            print(Fore.LIGHTBLUE_EX + "Seleccione la opción de temperatura:")
            print("1. Celcius a Fahrenheit")
            print("2. Fahrenheit a Celcius")
            opcion_temp = int(input("Ingrese su opción: "))
        
            if opcion_temp == 1:
                celcius = float(input("Ingrese la temperatura en Celcius: "))
                calculadora = Calculadora(celcius=celcius)
                resultado = calculadora.convertir_celcius_a_fahrenheit()
                print(Fore.LIGHTBLUE_EX + f"{celcius} grados Celcius son {resultado} grados Fahrenheit")
            elif opcion_temp == 2:
                fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
                calculadora = Calculadora(fahrenheit=fahrenheit)
                resultado = calculadora.convertir_fahrenheit_a_celcius()
                print(Fore.LIGHTBLUE_EX + f"{fahrenheit} grados Fahrenheit son {resultado} grados Celcius")
            else:
                print(Fore.RED +  "Opción no válida")

        elif opcion == 2:     
            print(Fore.MAGENTA + "Ingrese su opcion de longitud:")
            print(Fore.MAGENTA + "1. Kilometros ")
            print(Fore.MAGENTA + "2. Metros ")
            print(Fore.MAGENTA + "3. Centimetros ")
            print(Fore.MAGENTA + "4. Milimetros ")
            print(Fore.MAGENTA + "5. Millas ")
            print(Fore.MAGENTA + "6. Pies ")
            print(Fore.MAGENTA + "7. Pulgadas ")
            opcion_longitud = int(input("Ingrese su opción: "))
           
            if opcion_longitud == 1:
                print(Fore.MAGENTA + "Convertir Kilometros a Metros")
                print(Fore.MAGENTA + "Convertir Kilometros a Centimetros")
                print(Fore.MAGENTA + "Convertir Kilometros a Milimetros")
                print(Fore.MAGENTA + "Convertir Kilometros a Millas")
                print(Fore.MAGENTA + "Convertir Kilometros a Pies")
                print(Fore.MAGENTA + "Convertir Kilometros a Pulgadas")
                kilometros = float(input("Ingrese la longitud en kilometros: "))
                
                print("¿A qué unidad lo quieres convertir? (1: Metros, 2: Centímetros, 3: Milímetros, 4: Millas, 5: Pies, 6: Pulgadas)")
                kilometros = int(input("Ingrese opción de destino: "))
                
                if kilometros == 1:
                    resultado = calculadora.convertir_longitud(kilometros, 1000)
                    print(f"{kilometros} kilometros son {resultado} metros")
                if kilometros == 2:
                    resultado = calculadora.convertir_longitud(kilometros, 100000)
                    print(f"{kilometros} kilometros son {resultado} centimetros")
                if kilometros == 3:
                    resultado = calculadora.convertir_longitud(kilometros, 1000000)
                    print(f"{kilometros} kilometros son {resultado} milimetros")
                if kilometros == 4:
                    resultado = calculadora.convertir_longitud(kilometros, 0.621371)
                    print(f"{kilometros} kilometros son {resultado} millas")
                if kilometros == 5:
                    resultado = calculadora.convertir_longitud(kilometros, 3280.84)
                    print(f"{kilometros} kilometros son {resultado} pies")
                if kilometros == 6:
                    resultado = calculadora.convertir_longitud(kilometros, 39370.1)
                    print(f"{kilometros} kilometros son {resultado} pulgadas")

            elif opcion_longitud == 2:
                print(Fore.MAGENTA + "Convertir Metros a Kilometros")
                print(Fore.MAGENTA + "Convertir Metros a Centimetros")
                print(Fore.MAGENTA + "Convertir Metros a Milimetros")
                print(Fore.MAGENTA + "Convertir Metros a Millas")
                print(Fore.MAGENTA + "Convertir Metros a Pies")
                print(Fore.MAGENTA + "Convertir Metros a Pulgadas")
                metros = float(input("Ingrese la longitud en metros: "))
                
                print("¿A qué unidad lo quieres convertir? (1: Kilómetros, 2: Centímetros, 3: Milímetros, 4: Millas, 5: Pies, 6: Pulgadas)")
                metros = int(input("Ingrese opción de destino: "))
                
                if metros == 1:
                    resultado = calculadora.convertir_longitud(metros, 0.001)
                    print(Fore.MAGENTA + f"{metros} metros son {resultado} kilometros")
                if metros == 2:
                    resultado = calculadora.convertir_longitud(metros, 100)
                    print(Fore.MAGENTA + f"{metros} metros son {resultado} centimetros") 
                if metros == 3:
                    resultado = calculadora.convertir_longitud(metros, 1000)
                    print(Fore.MAGENTA + f"{metros} metros son {resultado} milimetros")
                if metros == 4:
                    resultado = calculadora.convertir_longitud(metros, 0.000621371)
                    print(Fore.MAGENTA + f"{metros} metros son {resultado} millas")
                if metros == 5:
                    resultado = calculadora.convertir_longitud(metros, 3.28084)
                    print(Fore.MAGENTA + f"{metros} metros son {resultado} pies")
                if metros == 6:
                    resultado = calculadora.convertir_longitud(metros, 39.3701)
                    print(Fore.MAGENTA + f"{metros} metros son {resultado} pulgadas")

            elif opcion_longitud == 3:
                print(Fore.MAGENTA + "Convertir Centimetros a Kilometros")
                print(Fore.MAGENTA + "Convertir Centimetros a Metros")
                print(Fore.MAGENTA + "Convertir Centimetros a Milimetros")
                print(Fore.MAGENTA + "Convertir Centimetros a Millas")
                print(Fore.MAGENTA + "Convertir Centimetros a Pies")
                print(Fore.MAGENTA + "Convertir Centimetros a Pulgadas")
                centimetros = float(input("Ingrese la longitud en centimetros: "))
                
                print("¿A qué unidad lo quieres convertir? (1: Kilómetros, 2: Metros, 3: Milímetros, 4: Millas, 5: Pies, 6: Pulgadas)")
                centimetros= int(input("Ingrese opción de destino: "))
                
                if centimetros == 1:
                    resultado = calculadora.convertir_longitud(centimetros, 0.00001)
                    print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} kilometros")
                if centimetros == 2:
                    resultado = calculadora.convertir_longitud(centimetros, 0.01)
                    print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} metros") 
                if centimetros == 3:
                    resultado = calculadora.convertir_longitud(centimetros, 10)
                    print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} milimetros")
                if centimetros == 4:
                    resultado = calculadora.convertir_longitud(centimetros, 0.0000062137)
                    print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} millas")
                if centimetros == 5:
                    resultado = calculadora.convertir_longitud(centimetros, 0.0328084)
                    print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} pies")
                if centimetros == 6:
                    resultado = calculadora.convertir_longitud(centimetros, 0.393701)
                    print(Fore.MAGENTA + f"{centimetros} centimetros son {resultado} pulgadas") 

            elif opcion_longitud == 4:
                print(Fore.MAGENTA + "Convertir Milimetros a Kilometros")
                print(Fore.MAGENTA + "Convertir Milimetros a Metros")
                print(Fore.MAGENTA + "Convertir Milimetros a Centimetros")
                print(Fore.MAGENTA + "Convertir Milimetros a Millas")
                print(Fore.MAGENTA + "Convertir Milimetros a Pies")
                print(Fore.MAGENTA + "Convertir Milimetros a Pulgadas")
                milimetros = float(input("Ingrese la longitud en milimetros: "))
                
                print("¿A qué unidad lo quieres convertir? (1: Kilómetros, 2: Metros, 3: Centímetros, 4: Millas, 5: Pies, 6: Pulgadas)")
                milimetros = int(input("Ingrese opción de destino: "))
                
                if milimetros == 1:
                    resultado = calculadora.convertir_longitud(milimetros, 0.000001)
                    print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} kilometros")
                if milimetros == 2:
                    resultado = calculadora.convertir_longitud(milimetros, 0.001)
                    print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} metros") 
                if milimetros == 3:
                    resultado = calculadora.convertir_longitud(milimetros, 0.1)
                    print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} centimetros")
                if milimetros == 4:
                    resultado = calculadora.convertir_longitud(milimetros, 0.00000062137)
                    print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} millas")
                if milimetros == 5:
                    resultado = calculadora.convertir_longitud(milimetros, 0.00328084)
                    print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} pies")
                if milimetros == 6:
                    resultado = calculadora.convertir_longitud(milimetros, 0.0393701)
                    print(Fore.MAGENTA + f"{milimetros} milimetros son {resultado} pulgadas")

            
            elif opcion_longitud == 5:
                print(Fore.MAGENTA + "Convertir Millas a Kilometros")
                print(Fore.MAGENTA + "Convertir Millas a Metros")
                print(Fore.MAGENTA + "Convertir Millas a Centimetros")
                print(Fore.MAGENTA + "Convertir Millas a Milimetros")
                print(Fore.MAGENTA + "Convertir Millas a Pies")
                print(Fore.MAGENTA + "Convertir Millas a Pulgadas")
                millas = float(input("Ingrese la longitud en millas: "))
                
                print("¿A qué unidad lo quieres convertir? (1: Kilómetros, 2: Metros, 3: Centímetros, 4: Milímetros, 5: Pies, 6: Pulgadas)")
                millas = int(input("Ingrese opción de destino: "))
                
                if millas == 1:
                    resultado = calculadora.convertir_longitud(millas, 1.60934)
                    print(Fore.MAGENTA + f"{millas} millas son {resultado} kilometros")
                if millas == 2:
                    resultado = calculadora.convertir_longitud(millas, 1609.34)
                    print(Fore.MAGENTA + f"{millas} millas son {resultado} metros") 
                if millas == 3:
                    resultado = calculadora.convertir_longitud(millas, 160934)
                    print(Fore.MAGENTA + f"{millas} millas son {resultado} centimetros")
                if millas == 4:
                    resultado = calculadora.convertir_longitud(millas, 1609344)
                    print(Fore.MAGENTA + f"{millas} millas son {resultado} milimetros")
                if millas == 5:
                    resultado = calculadora.convertir_longitud(millas, 5280)
                    print(Fore.MAGENTA + f"{millas} millas son {resultado} pies")
                if millas == 6:
                    resultado = calculadora.convertir_longitud(millas, 63360)
                    print(Fore.MAGENTA + f"{millas} millas son {resultado} pulgadas")

            elif opcion_longitud == 6:
                print(Fore.MAGENTA + "Convertir Pies a Kilometros")
                print(Fore.MAGENTA + "Convertir Pies a Metros")
                print(Fore.MAGENTA + "Convertir Pies a Centimetros")
                print(Fore.MAGENTA + "Convertir Pies a Milimetros")
                print(Fore.MAGENTA + "Convertir Pies a Millas")
                print(Fore.MAGENTA + "Convertir Pies a Pulgadas")
                pies = float(input("Ingrese la longitud en pies: "))
                
                print("¿A qué unidad lo quieres convertir? (1: Kilómetros, 2: Metros, 3: Centímetros, 4: Milímetros, 5: Millas, 6: Pulgadas)")
                pies = int(input("Ingrese opción de destino: "))
                
                if pies == 1:
                    resultado = calculadora.convertir_longitud(pies, 0.0003048)
                    print(Fore.MAGENTA + f"{pies} pies son {resultado} kilometros")
                if pies == 2:
                    resultado = calculadora.convertir_longitud(pies, 0.3048)
                    print(Fore.MAGENTA + f"{pies} pies son {resultado} metros") 
                if pies == 3:
                    resultado = calculadora.convertir_longitud(pies, 30.48)
                    print(Fore.MAGENTA + f"{pies} pies son {resultado} centimetros")
                if pies == 4:
                    resultado = calculadora.convertir_longitud(pies, 304.8)
                    print(Fore.MAGENTA + f"{pies} pies son {resultado} milimetros")
                if pies == 5:
                    resultado = calculadora.convertir_longitud(pies, 0.000189394)
                    print(Fore.MAGENTA + f"{pies} pies son {resultado} millas")
                if pies == 6:
                    resultado = calculadora.convertir_longitud(pies, 12)
                    print(Fore.MAGENTA + f"{pies} pies son {resultado} pulgadas")

            elif opcion_longitud == 7:
                print(Fore.MAGENTA + "Convertir Pulgadas a Kilometros")
                print(Fore.MAGENTA + "Convertir Pulgadas a Metros")
                print(Fore.MAGENTA + "Convertir Pulgadas a Centimetros")
                print(Fore.MAGENTA + "Convertir Pulgadas a Milimetros")
                print(Fore.MAGENTA + "Convertir Pulgadas a Millas")
                print(Fore.MAGENTA + "Convertir Pulgadas a Pies")
                pulgadas = float(input("Ingrese la longitud en pulgadas: "))
                
                print("¿A qué unidad lo quieres convertir? (1: Kilómetros, 2: Metros, 3: Centímetros, 4: Milímetros, 5: Millas, 6: Pies)")
                pulgadas = int(input("Ingrese opción de destino: "))
                
                if pulgadas == 1:
                    resultado = calculadora.convertir_longitud(pulgadas, 0.0000254)
                    print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} kilometros")
                if pulgadas == 2:
                    resultado = calculadora.convertir_longitud(pulgadas, 0.0254)
                    print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} metros") 
                if pulgadas == 3:
                    resultado = calculadora.convertir_longitud(pulgadas, 2.54)
                    print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} centimetros")
                if pulgadas == 4:
                    resultado = calculadora.convertir_longitud(pulgadas, 25.4)
                    print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} milimetros")
                if pulgadas == 5:
                    resultado = calculadora.convertir_longitud(pulgadas, 0.000015783)
                    print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} millas")
                if pulgadas == 6:
                    resultado = calculadora.convertir_longitud(pulgadas, 0.0833333)
                    print(Fore.MAGENTA + f"{pulgadas} pulgadas son {resultado} pies")
