import tkinter as tk
from tkinter import PhotoImage

# Fatores de emissão aproximados (em kg CO₂)
CO2_CARRO = 0.21  # kg CO₂ por km
CO2_TRANS_PUBLICO = 0.10  # kg CO₂ por km
CO2_ENERGIA = 0.233  # kg CO₂ por kWh


def calculate_footprint():
    try:
        # Recebe as entradas e converte para float
        km_carro = float(entry_km_car.get())
        km_transporte = float(entry_km_transport.get())
        consumo_energia = float(entry_energy.get())

        # Cálculo de emissões
        emissao_carro = km_carro * CO2_CARRO
        emissao_transporte = km_transporte * CO2_TRANS_PUBLICO
        emissao_energia = consumo_energia * CO2_ENERGIA

        # Total de emissões
        total_emissao = emissao_carro + emissao_transporte + emissao_energia

        # Exibe o resultado formatado
        label_result.config(
            text=f"🌍 Pegada de Carbono Estimada 🌍\n"
                 f"Carro: {emissao_carro:.2f} kg CO₂\n"
                 f"Transporte Público: {emissao_transporte:.2f} kg CO₂\n"
                 f"Consumo de Energia: {emissao_energia:.2f} kg CO₂\n"
                 f"Total: {total_emissao:.2f} kg CO₂",
            fg="dark green"
        )
    except ValueError:
        label_result.config(text="🚫 Por favor, insira valores numéricos válidos!", fg="red")


# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de Pegada de Carbono 🌍")
janela.geometry("500x500")
janela.config(bg="#A7C7E7")  # Cor de fundo azul claro

# Imagem ou ícone
# Certifique-se de ter um arquivo de imagem "earth_icon.png" no mesmo diretório
try:
    img = PhotoImage(file="earth_icon.png")
    label_img = tk.Label(janela, image=img, bg="#A7C7E7")
    label_img.pack(pady=10)
except:
    pass

# Título e instrução
label_titulo = tk.Label(janela, text="Calculadora de Pegada de Carbono", font=("Comic Sans MS", 18, "bold"),
                        bg="#A7C7E7", fg="#2C5F2D")
label_titulo.pack(pady=10)

label_instrucao = tk.Label(janela, text="Insira os dados abaixo para calcular sua pegada de carbono:",
                           font=("Arial", 12), bg="#A7C7E7")
label_instrucao.pack(pady=5)

# Entrada para distância percorrida de carro
label_km_car = tk.Label(janela, text="Distância percorrida de carro (km):", font=("Arial", 10), bg="#A7C7E7")
label_km_car.pack()
entry_km_car = tk.Entry(janela, font=("Arial", 12), width=15)
entry_km_car.pack(pady=5)

# Entrada para distância percorrida em transporte público
label_km_transport = tk.Label(janela, text="Distância percorrida em transporte público (km):", font=("Arial", 10),
                              bg="#A7C7E7")
label_km_transport.pack()
entry_km_transport = tk.Entry(janela, font=("Arial", 12), width=15)
entry_km_transport.pack(pady=5)

# Entrada para consumo de energia elétrica
label_energy = tk.Label(janela, text="Consumo de energia elétrica (kWh):", font=("Arial", 10), bg="#A7C7E7")
label_energy.pack()
entry_energy = tk.Entry(janela, font=("Arial", 12), width=15)
entry_energy.pack(pady=5)


# Botão para calcular (com hover)
def on_enter(e):
    button_calculate.config(bg="#69A197")


def on_leave(e):
    button_calculate.config(bg="#87CEFA")


button_calculate = tk.Button(
    janela,
    text="Calcular Pegada de Carbono",
    font=("Comic Sans MS", 12, "bold"),
    bg="#87CEFA",
    fg="black",
    command=calculate_footprint,  # Corrigido para chamar a função sem parênteses
    activebackground="#69A197",
    relief="raised",
    cursor="hand2"
)
button_calculate.pack(pady=15)
button_calculate.bind("<Enter>", on_enter)
button_calculate.bind("<Leave>", on_leave)

# Label para exibir o resultado
label_result = tk.Label(janela, text="", font=("Arial", 12), bg="#A7C7E7")
label_result.pack(pady=20)

# Loop principal da aplicação
janela.mainloop()
