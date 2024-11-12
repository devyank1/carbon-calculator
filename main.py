import tkinter as tk
from tkinter import PhotoImage

# FACTORS OF A EMISSION GAS
CO2_CAR = 0.21  # kg CO₂ per km
CO2_TRANS_PUBLIC = 0.10  # kg CO₂ per km
CO2_ENERGY = 0.233  # kg CO₂ per kWh


def calculate_footprint():
    try:
        km_car = float(entry_km_car.get())
        km_transport = float(entry_km_transport.get())
        consume_energy = float(entry_energy.get())

        # EMISSION CALC
        emission_car = km_car * CO2_CAR
        emission_transport = km_transport * CO2_TRANS_PUBLIC
        emission_energy = consume_energy * CO2_ENERGY

        # TOTAL EMISSION
        total_emission = emission_car + emission_energy + emission_transport

        # EXHIBIT THE TOTAL
        label_result.config(
            text=f"🌍 Pegada de Carbono Estimada 🌍\n"
                 f"Carro: {emission_car:.2f} kg CO₂\n"
                 f"Transporte Público: {emission_transport:.2f} kg CO₂\n"
                 f"Consumo de Energia: {emission_energy:.2f} kg CO₂\n"
                 f"Total: {total_emission:.2f} kg CO₂",
            fg="dark green"
        )
    except ValueError:
        label_result.config(text="🚫 Por favor, insira valores numéricos válidos!", fg="red")


# MAIN WINDOW CONFIGURATION
window = tk.Tk()
window.title("Calculadora de Pegada de Carbono 🌍")
window.geometry("500x500")
window.config(bg="#A7C7E7")  # Cor de fundo azul claro

try:
    img = PhotoImage(file="earth_icon.png")
    label_img = tk.Label(window, image=img, bg="#A7C7E7")
    label_img.pack(pady=10)
except:
    pass

# INSTRUCTION AND TITLE
label_title = tk.Label(window, text="Calculadora de Pegada de Carbono", font=("Comic Sans MS", 18, "bold"),
                        bg="#A7C7E7", fg="#2C5F2D")
label_title.pack(pady=10)

label_instruction = tk.Label(window, text="Insira os dados abaixo para calcular sua pegada de carbono:",
                           font=("Arial", 12), bg="#A7C7E7")
label_instruction.pack(pady=5)

# ENTRY DISTANCE CAR
label_km_car = tk.Label(window, text="Distância percorrida de carro (km):", font=("Arial", 10), bg="#A7C7E7")
label_km_car.pack()
entry_km_car = tk.Entry(window, font=("Arial", 12), width=15)
entry_km_car.pack(pady=5)

# ENTRY DISTANCE TRANSPORT PUBLIC
label_km_transport = tk.Label(window, text="Distância percorrida em transporte público (km):", font=("Arial", 10),
                              bg="#A7C7E7")
label_km_transport.pack()
entry_km_transport = tk.Entry(window, font=("Arial", 12), width=15)
entry_km_transport.pack(pady=5)

# ENTRY ELECTRIC CONSUME
label_energy = tk.Label(window, text="Consumo de energia elétrica (kWh):", font=("Arial", 10), bg="#A7C7E7")
label_energy.pack()
entry_energy = tk.Entry(window, font=("Arial", 12), width=15)
entry_energy.pack(pady=5)


# Botão para calcular (com hover)
def on_enter(e):
    button_calculate.config(bg="#69A197")


def on_leave(e):
    button_calculate.config(bg="#87CEFA")


button_calculate = tk.Button(
    window,
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
label_result = tk.Label(window, text="", font=("Arial", 12), bg="#A7C7E7")
label_result.pack(pady=20)

# Loop principal da aplicação
window.mainloop()
