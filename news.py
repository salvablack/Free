import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser

# Función para obtener noticias sobre un tema específico
def obtener_noticias_tema(tema):
    # URL de Google News en español para la búsqueda de noticias sobre el tema ingresado
    url = f"https://news.google.com/rss/search?q={tema}&hl=es-419&gl=ES&ceid=ES:es"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    
    noticias = []
    
    for item in soup.find_all("item", limit=100):  # Limite de 100 noticias
        titulo = item.title.text
        enlace = item.link.text
        noticias.append((titulo, enlace))
    
    return noticias

# Función para abrir el enlace en el navegador
def abrir_enlace(enlace):
    webbrowser.open(enlace)

# Crear la interfaz gráfica con Tkinter
def mostrar_noticias():
    noticias = []  # Lista para almacenar las noticias obtenidas
    
    def buscar_noticias():
        nonlocal noticias  # Permite modificar la lista de noticias en la función on_select
        tema = entry.get()  # Obtener el tema ingresado por el usuario
        noticias = obtener_noticias_tema(tema)
        
        listbox.delete(0, tk.END)  # Limpiar la lista antes de mostrar nuevas noticias
        
        for i, (titulo, enlace) in enumerate(noticias, 1):
            listbox.insert(tk.END, f"{i}. {titulo}")

    root = tk.Tk()
    root.title("Noticias por Tema")
    
    # Configuración de colores
    root.configure(bg="black")  # Fondo negro
    
    frame = tk.Frame(root, bg="black")  # Fondo negro para el frame
    frame.pack(fill=tk.BOTH, expand=True)

    label = tk.Label(frame, text="Ingrese un tema:", bg="black", fg="cyan")
    label.pack(pady=10)
    
    entry = tk.Entry(frame, width=50)
    entry.pack(pady=10)
    
    button = tk.Button(frame, text="Buscar Noticias", command=buscar_noticias, bg="cyan", fg="black")
    button.pack(pady=10)
    
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=100, height=25, 
                         bg="black", fg="cyan", selectbackground="gray", selectforeground="black")
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
    
    # Función para manejar el clic en la lista
    def on_select(event):
        seleccion = listbox.curselection()
        if seleccion:
            index = seleccion[0]
            _, enlace = noticias[index]
            abrir_enlace(enlace)
    
    listbox.bind("<<ListboxSelect>>", on_select)
    
    root.mainloop()

# Ejecutar el programa
if __name__ == "__main__":
    mostrar_noticias()
