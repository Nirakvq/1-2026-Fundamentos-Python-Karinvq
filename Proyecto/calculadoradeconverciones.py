import gradio as gr

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

calculadora = Calculadora()

def menu_temperatura(opcion_temp, valor):
    if opcion_temp == 1:
        calculadora.celcius = valor
        resultado = calculadora.convertir_celcius_a_fahrenheit()
        return f"{valor} grados Celcius son {resultado} grados Fahrenheit"
    elif opcion_temp == 2:
        calculadora.fahrenheit = valor
        resultado = calculadora.convertir_fahrenheit_a_celcius()
        return f"{valor} grados Fahrenheit son {resultado} grados Celcius"
    else:
        return "Opción no válida"

def menu_longitud(opcion_longitud, valor, opcion_destino):
    if opcion_longitud == 1:
        if opcion_destino == 1:
            resultado = calculadora.convertir_longitud(valor, 1000)
            return f"{valor} kilometros son {resultado} metros"
        if opcion_destino == 2:
            resultado = calculadora.convertir_longitud(valor, 100000)
            return f"{valor} kilometros son {resultado} centimetros"
        if opcion_destino == 3:
            resultado = calculadora.convertir_longitud(valor, 1000000)
            return f"{valor} kilometros son {resultado} milimetros"
        if opcion_destino == 4:
            resultado = calculadora.convertir_longitud(valor, 0.621371)
            return f"{valor} kilometros son {resultado} millas"
        if opcion_destino == 5:
            resultado = calculadora.convertir_longitud(valor, 3280.84)
            return f"{valor} kilometros son {resultado} pies"
        if opcion_destino == 6:
            resultado = calculadora.convertir_longitud(valor, 39370.1)
            return f"{valor} kilometros son {resultado} pulgadas"

    elif opcion_longitud == 2:
        if opcion_destino == 1:
            resultado = calculadora.convertir_longitud(valor, 0.001)
            return f"{valor} metros son {resultado} kilometros"
        if opcion_destino == 2:
            resultado = calculadora.convertir_longitud(valor, 100)
            return f"{valor} metros son {resultado} centimetros" 
        if opcion_destino == 3:
            resultado = calculadora.convertir_longitud(valor, 1000)
            return f"{valor} metros son {resultado} milimetros"
        if opcion_destino == 4:
            resultado = calculadora.convertir_longitud(valor, 0.000621371)
            return f"{valor} metros son {resultado} millas"
        if opcion_destino == 5:
            resultado = calculadora.convertir_longitud(valor, 3.28084)
            return f"{valor} metros son {resultado} pies"
        if opcion_destino == 6:
            resultado = calculadora.convertir_longitud(valor, 39.3701)
            return f"{valor} metros son {resultado} pulgadas"

    elif opcion_longitud == 3:
        if opcion_destino == 1:
            resultado = calculadora.convertir_longitud(valor, 0.00001)
            return f"{valor} centimetros son {resultado} kilometros"
        if opcion_destino == 2:
            resultado = calculadora.convertir_longitud(valor, 0.01)
            return f"{valor} centimetros son {resultado} metros" 
        if opcion_destino == 3:
            resultado = calculadora.convertir_longitud(valor, 10)
            return f"{valor} centimetros son {resultado} milimetros"
        if opcion_destino == 4:
            resultado = calculadora.convertir_longitud(valor, 0.0000062137)
            return f"{valor} centimetros son {resultado} millas"
        if opcion_destino == 5:
            resultado = calculadora.convertir_longitud(valor, 0.0328084)
            return f"{valor} centimetros son {resultado} pies"
        if opcion_destino == 6:
            resultado = calculadora.convertir_longitud(valor, 0.393701)
            return f"{valor} centimetros son {resultado} pulgadas" 

    elif opcion_longitud == 4:
        if opcion_destino == 1:
            resultado = calculadora.convertir_longitud(valor, 0.000001)
            return f"{valor} milimetros son {resultado} kilometros"
        if opcion_destino == 2:
            resultado = calculadora.convertir_longitud(valor, 0.001)
            return f"{valor} milimetros son {resultado} metros" 
        if opcion_destino == 3:
            resultado = calculadora.convertir_longitud(valor, 0.1)
            return f"{valor} milimetros son {resultado} centimetros"
        if opcion_destino == 4:
            resultado = calculadora.convertir_longitud(valor, 0.00000062137)
            return f"{valor} milimetros son {resultado} millas"
        if opcion_destino == 5:
            resultado = calculadora.convertir_longitud(valor, 0.00328084)
            return f"{valor} milimetros son {resultado} pies"
        if opcion_destino == 6:
            resultado = calculadora.convertir_longitud(valor, 0.0393701)
            return f"{valor} milimetros son {resultado} pulgadas"

    elif opcion_longitud == 5:
        if opcion_destino == 1:
            resultado = calculadora.convertir_longitud(valor, 1.60934)
            return f"{valor} millas son {resultado} kilometros"
        if opcion_destino == 2:
            resultado = calculadora.convertir_longitud(valor, 1609.34)
            return f"{valor} millas son {resultado} metros" 
        if opcion_destino == 3:
            resultado = calculadora.convertir_longitud(valor, 160934)
            return f"{valor} millas son {resultado} centimetros"
        if opcion_destino == 4:
            resultado = calculadora.convertir_longitud(valor, 1609344)
            return f"{valor} millas son {resultado} milimetros"
        if opcion_destino == 5:
            resultado = calculadora.convertir_longitud(valor, 5280)
            return f"{valor} millas son {resultado} pies"
        if opcion_destino == 6:
            resultado = calculadora.convertir_longitud(valor, 63360)
            return f"{valor} millas son {resultado} pulgadas"

    elif opcion_longitud == 6:
        if opcion_destino == 1:
            resultado = calculadora.convertir_longitud(valor, 0.0003048)
            return f"{valor} pies son {resultado} kilometros"
        if opcion_destino == 2:
            resultado = calculadora.convertir_longitud(valor, 0.3048)
            return f"{valor} pies son {resultado} metros" 
        if opcion_destino == 3:
            resultado = calculadora.convertir_longitud(valor, 30.48)
            return f"{valor} pies son {resultado} centimetros"
        if opcion_destino == 4:
            resultado = calculadora.convertir_longitud(valor, 304.8)
            return f"{valor} pies son {resultado} milimetros"
        if opcion_destino == 5:
            resultado = calculadora.convertir_longitud(valor, 0.000189394)
            return f"{valor} pies son {resultado} millas"
        if opcion_destino == 6:
            resultado = calculadora.convertir_longitud(valor, 12)
            return f"{valor} pies son {resultado} pulgadas"

    elif opcion_longitud == 7:
        if opcion_destino == 1:
            resultado = calculadora.convertir_longitud(valor, 0.0000254)
            return f"{valor} pulgadas son {resultado} kilometros"
        if opcion_destino == 2:
            resultado = calculadora.convertir_longitud(valor, 0.0254)
            return f"{valor} pulgadas son {resultado} metros" 
        if opcion_destino == 3:
            resultado = calculadora.convertir_longitud(valor, 2.54)
            return f"{valor} pulgadas son {resultado} centimetros"
        if opcion_destino == 4:
            resultado = calculadora.convertir_longitud(valor, 25.4)
            return f"{valor} pulgadas son {resultado} milimetros"
        if opcion_destino == 5:
            resultado = calculadora.convertir_longitud(valor, 0.000015783)
            return f"{valor} pulgadas son {resultado} millas"
        if opcion_destino == 6:
            resultado = calculadora.convertir_longitud(valor, 0.0833333)
            return f"{valor} pulgadas son {resultado} pies"
    return "Opción no válida"

with gr.Blocks() as interfaz:
    gr.Markdown("# Bienvenido al convertidor de unidades")
    
    with gr.Tab("1. Temperatura"):
        opcion_temp = gr.Radio(choices=[( "1. Celcius a Fahrenheit", 1), ("2. Fahrenheit a Celcius", 2)], label="Seleccione la opción de temperatura:")
        valor_temp = gr.Number(label="Ingrese la temperatura:")
        btn_temp = gr.Button("Calcular")
        salida_temp = gr.Textbox(label="Resultado")
        btn_temp.click(fn=menu_temperatura, inputs=[opcion_temp, valor_temp], outputs=salida_temp)
        
    with gr.Tab("2. Longitud"):
        opcion_longitud = gr.Dropdown(
            choices=[
                ("1. Kilometros", 1), ("2. Metros", 2), ("3. Centimetros", 3), 
                ("4. Milimetros", 4), ("5. Millas", 5), ("6. Pies", 6), ("7. Pulgadas", 7)
            ], 
            label="Ingrese su opcion de longitud origen:"
        )
        valor_long = gr.Number(label="Ingrese la longitud:")
        opcion_destino = gr.Radio(
            choices=[
                ("1. Metros / Kilómetros", 1), ("2. Centímetros / Metros", 2), ("3. Milímetros / Centímetros", 3), 
                ("4. Millas / Milímetros", 4), ("5. Pies / Millas", 5), ("6. Pulgadas / Pies", 6)
            ], 
            label="¿A qué unidad lo quieres convertir? (Opción de destino):"
        )
        btn_long = gr.Button("Calcular")
        salida_long = gr.Textbox(label="Resultado")
        btn_long.click(fn=menu_longitud, inputs=[opcion_longitud, valor_long, opcion_destino], outputs=salida_long)

if __name__ == "__main__":
    interfaz.launch()
