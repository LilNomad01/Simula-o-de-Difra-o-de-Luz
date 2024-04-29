import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def double_sided_slit(x, slit_width, slit_thickness):
    return np.where((abs(x) <= slit_width / 2) & (abs(x) >= (slit_width / 2 - slit_thickness)), 1, 0)

def incident_wave(x, wavelength):
    return np.sin(2 * np.pi * x / wavelength)

def diffraction(x):
    return np.abs(np.fft.fftshift(np.fft.fft(np.fft.fftshift(x))))

def simulate_diffraction(wavelength, slit_width, slit_thickness, distance=10.0, screen_width=20, qntd_fendas=1):
    screen_pos = np.linspace(-screen_width / 2, screen_width / 2, 1000)
    intensity = np.zeros_like(screen_pos)
    for i in range(qntd_fendas):
        f = double_sided_slit(screen_pos - i * screen_width / qntd_fendas, slit_width, slit_thickness)
        intensity += diffraction(f * incident_wave(screen_pos - i * screen_width / qntd_fendas, wavelength))
    intensity /= np.max(intensity)
    
    #cria o grafico
    plt.plot(screen_pos, intensity)
    plt.fill_between(screen_pos, intensity, alpha=0.5)
    plt.xlabel('Posição na Tela')
    plt.ylabel('Intensidade')
    plt.title('Padrão de Difração em Fenda de Dupla Face')
    plt.show()

def open_input_window():
    input_window = tk.Tk()
    input_window.title("Entrada de Dados")

    tk.Label(input_window, text="Comprimento de Onda:").pack()
    wavelength_entry = tk.Entry(input_window)
    wavelength_entry.pack()

    tk.Label(input_window, text="Largura da Fenda:").pack()
    slit_width_entry = tk.Entry(input_window)
    slit_width_entry.pack()

    tk.Label(input_window, text="Espessura da Fenda:").pack()
    slit_thickness_entry = tk.Entry(input_window)
    slit_thickness_entry.pack()

    tk.Label(input_window, text="Distância até a Tela:").pack()
    distance_entry = tk.Entry(input_window)
    distance_entry.pack()

    tk.Label(input_window, text="Largura da Tela:").pack()
    screen_width_entry = tk.Entry(input_window)
    screen_width_entry.pack()

    tk.Label(input_window, text="Número de Fendas:").pack()
    qntd_fendas_entry = tk.Entry(input_window)
    qntd_fendas_entry.pack()

    simulate_button = tk.Button(input_window, text="Simular Difração",
                                command=lambda: simulate_diffraction(float(wavelength_entry.get()),
                                                                      float(slit_width_entry.get()),
                                                                      float(slit_thickness_entry.get()),
                                                                      float(distance_entry.get()),
                                                                      float(screen_width_entry.get()),
                                                                      int(qntd_fendas_entry.get())))
    simulate_button.pack()

    input_window.mainloop()

main_window = tk.Tk()
main_window.title("Simulação de Difração")

simulate_button = tk.Button(main_window, text="Abrir Entrada de Dados", command=open_input_window)
simulate_button.pack()

main_window.mainloop()
