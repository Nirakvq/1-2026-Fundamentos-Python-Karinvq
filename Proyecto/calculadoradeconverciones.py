
import math
import gradio as gr

def calcular_propiedades(radio, unidad_medida):
    if radio <= 0:
        return "El radio debe ser un número mayor a cero.", "", "", ""
    
    # Cálculos geométricos básicos
    # Perímetro de la circunferencia: C = 2 * pi * r
    perimetro = 2 * math.pi * radio
    
    # Área del círculo: A = pi * r^2
    area = math.pi * (radio ** 2)
    
    # Volumen de la esfera: V = (4/3) * pi * r^3
    volumen = (4 / 3) * math.pi * (radio ** 3)
    
    # Formatear los resultados con su respectiva unidad
    res_perimetro = f"{perimetro:.4f} {unidad_medida}"
    res_area = f"{area:.4f} {unidad_medida}²"
    res_volumen = f"{volumen:.4f} {unidad_medida}³"
    
    return "Cálculo exitoso", res_perimetro, res_area, res_volumen


with gr.Blocks(title="Calculadora Geométrica Base Radio - Beta") as demo:
    gr.Markdown("# 📐 Calculadora de Unidades Basada en Radio")
    gr.Markdown("### *Versión de Prueba (Beta)*")
    gr.Markdown("Introduce el radio y la unidad de medida para calcular instantáneamente el perímetro, área y volumen correspondientes.")
    
    with gr.Row():
        with gr.Column():
            input_radio = gr.Number(label="Valor del Radio", value=1.0, precision=4)
            input_unidad = gr.Dropdown(
                choices=["cm", "m", "in", "ft"], 
                value="cm", 
                label="Unidad de Medida"
            )
            btn_calcular = gr.Button("Calcular", variant="primary")
            
        with gr.Column():
            output_status = gr.Textbox(label="Estado del Sistema")
            output_perimetro = gr.Textbox(label="Perímetro (Circunferencia)")
            output_area = gr.Textbox(label="Área (Círculo)")
            output_volumen = gr.Textbox(label="Volumen (Esfera)")
            
    # Conectar el botón con la función lógica
    btn_calcular.click(
        fn=calcular_propiedades,
        inputs=[input_radio, input_unidad],
        outputs=[output_status, output_perimetro, output_area, output_volumen]
    )

if __name__ == "__main__":
    demo.launch()