import tkinter as tk

def create_envelope():
    envelope = tk.Tk()
    envelope.title("Envelope")

    # Configurar el tamaño y posición de la ventana
    envelope.geometry("280x180+300+150")

    # Configurar el color de fondo
    envelope.configure(bg="#f9c5c8")

    # Configurar la sombra
    envelope.attributes('-alpha', 0.9)  # Opacidad
    envelope.attributes('-topmost', True)  # Siempre encima

    # Configurar la sombra (opcional, depende del sistema operativo)
    envelope.wm_attributes('-transparentcolor', '#f9c5c8')  

    # Crear una etiqueta en la ventana
    label = tk.Label(envelope, text="Contenido del sobre", font=("Arial", 12), bg="#f9c5c8")
    label.pack(pady=30)

    # Ejecutar el bucle principal
    envelope.mainloop()

# Llamar a la función para crear el sobre
create_envelope()
