import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

# Función para generar el código QR
def generar_qr():
    texto = entrada.get()
    if not texto:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa un texto o enlace.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    imagen = qr.make_image(fill_color="black", back_color="white")
    imagen.save("output/qr_code.png")

    mostrar_imagen("output/qr_code.png")
    messagebox.showinfo("QR generado", "El código QR ha sido guardado en /output.")

# Función para mostrar la imagen en la interfaz
def mostrar_imagen(ruta):
    img = Image.open(ruta)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    etiqueta_imagen.config(image=img_tk)
    etiqueta_imagen.image = img_tk

# Crear carpeta de salida si no existe
import os
if not os.path.exists("output"):
    os.makedirs("output")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("🎯 Generador de Códigos QR")
ventana.geometry("400x500")
ventana.resizable(False, False)

tk.Label(ventana, text="Texto o enlace para convertir:", font=("Arial", 12)).pack(pady=10)
entrada = tk.Entry(ventana, width=40, font=("Arial", 12))
entrada.pack(pady=5)

tk.Button(ventana, text="Generar QR", command=generar_qr, font=("Arial", 12)).pack(pady=10)

etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=20)

tk.Label(ventana, text="El QR se guarda como 'qr_code.png' en /output", font=("Arial", 10), fg="gray").pack(pady=10)

ventana.mainloop()
