import tkinter as tk
from cryptography.fernet import Fernet
import pyperclip

# Funciones para encriptar y desencriptar el texto
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Funciones para los botones
def generate_key():
    return Fernet.generate_key()

def encrypt_text():
    global key, text_entry, result_entry
    message = text_entry.get("1.0",'end-1c')
    encrypted_message = encrypt_message(message, key)
    result_entry.delete(0, tk.END)  # Limpiar el cuadro de texto antes de insertar
    result_entry.insert(0, encrypted_message)

def decrypt_text():
    global key, text_entry, result_entry
    encrypted_message = result_entry.get()
    decrypted_message = decrypt_message(encrypted_message.encode(), key)
    result_entry.delete(0, tk.END)  # Limpiar el cuadro de texto antes de insertar
    result_entry.insert(0, decrypted_message)

def copy_to_clipboard():
    global result_entry
    result = result_entry.get()
    pyperclip.copy(result)

# Configuración de la ventana
window = tk.Tk()
window.title("Encriptador / Desencriptador")

# Generar una clave aleatoria
key = generate_key()

# Etiqueta y entrada para el texto
text_label = tk.Label(window, text="Salvacrypter by Salva Rosales | Introduce el texto:")
text_label.pack()
text_entry = tk.Text(window)
text_entry.pack()

# Botones para encriptar y desencriptar
encrypt_button = tk.Button(window, text="Encriptar", command=encrypt_text)
encrypt_button.pack()
decrypt_button = tk.Button(window, text="Desencriptar", command=decrypt_text)
decrypt_button.pack()

# Cuadro de texto para mostrar el resultado
result_label = tk.Label(window, text="Texto encriptado:")
result_label.pack()
result_entry = tk.Entry(window, width=50)
result_entry.pack()

# Botón para copiar al portapapeles
copy_button = tk.Button(window, text="Copiar al portapapeles", command=copy_to_clipboard)
copy_button.pack()

# Ejecución de la ventana
window.mainloop()
