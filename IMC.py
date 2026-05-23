
print("Bienvenido a la aplicación de cálculo de IMC")


nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese su apellidos: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))


imc = peso / (altura ** 2)


if imc < 18.5:
    rango = "Bajo peso"
elif imc >= 18.5 and imc <= 24.9:
    rango = "Peso normal"
elif imc >= 25.0 and imc <= 29.9:
    rango = "Sobrepeso"
else:
    rango = "Obesidad"


print("\n--- Resultado ---")
print("Nombre completo:", nombre, apellidos)
print("Edad:", edad)
print("Su IMC es:", round(imc, 2))
print("Rango:", rango)_