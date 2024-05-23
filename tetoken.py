import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
import secrets
import jwt
import datetime
import random
import string
import pyperclip

class TokenGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Tokens")

        # Calcular el tamaño de la pantalla y el tamaño de la ventana
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        window_width = int(screen_width / 2 * 0.8)  # Reducir el tamaño en un 20%
        window_height = int(screen_height / 2 * 0.8)

        # Posicionar la ventana en el centro de la pantalla
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)
        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Ajustar el tamaño de la fuente
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=10)  # Establecer el tamaño de la fuente en 10

        # Widget para seleccionar el tipo de token
        self.token_type_var = tk.StringVar()
        self.token_type_var.set("Autenticación")
        self.token_type_label = tk.Label(root, text="Tipo de Token:", font=default_font)
        self.token_type_label.pack(padx=10, pady=(30, 5))
        self.token_type_menu = tk.OptionMenu(root, self.token_type_var, "Autenticación", "Seguridad", "Palabras clave")
        self.token_type_menu.config(font=default_font)
        self.token_type_menu.pack(padx=10, pady=5)

        # Etiqueta para mostrar el token generado
        self.token_label = tk.Label(root, text="Token generado:", font=default_font)
        self.token_label.pack(padx=10, pady=10)

        # Botón para generar el token
        self.generate_button = tk.Button(root, text="Generar Token", command=self.generate_token, font=default_font)
        self.generate_button.pack(padx=10, pady=5)

        # Botón para copiar el token al portapapeles
        self.copy_button = tk.Button(root, text="Copiar al portapapeles", command=self.copy_to_clipboard, font=default_font)
        self.copy_button.pack(padx=10, pady=5)

        # Botón para salir del script
        self.exit_button = tk.Button(root, text="Salir", command=root.quit, font=default_font)
        self.exit_button.pack(padx=10, pady=5)

    def generate_token(self):
        token_type = self.token_type_var.get()

        if token_type == "Autenticación":
            token_length = 16
            token = secrets.token_hex(token_length)
        elif token_type == "Seguridad":
            token_length = 16
            token = secrets.token_urlsafe(token_length)
        elif token_type == "Palabras clave":
            token_length = 12
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=token_length))

        # Mostrar el token generado en la etiqueta correspondiente
        self.token_label.config(text=f"Token generado: {token}")
        self.generated_token = token  # Almacenar el token generado

    def copy_to_clipboard(self):
        # Copiar el token al portapapeles
        pyperclip.copy(self.generated_token)
        messagebox.showinfo("Copiado", "Token copiado al portapapeles")

if __name__ == "__main__":
    root = tk.Tk()
    app = TokenGeneratorApp(root)
    root.mainloop()
