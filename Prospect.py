import tkinter as tk
import sqlite3
import csv

class EmpresaDBApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empresas")
        
        self.create_gui()
        self.create_database()
        self.actualizar_tabla()

    def create_gui(self):
        # Crear etiquetas y campos de entrada
        tk.Label(self.root, text="Nombre de la Empresa:").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Industria:").grid(row=1, column=0)
        self.industria_entry = tk.Entry(self.root)
        self.industria_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Tamaño de la Empresa:").grid(row=2, column=0)
        self.tamaño_entry = tk.Entry(self.root)
        self.tamaño_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Necesidades:").grid(row=3, column=0)
        self.necesidades_entry = tk.Entry(self.root)
        self.necesidades_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Prioridad:").grid(row=4, column=0)
        self.prioridad_entry = tk.Entry(self.root)
        self.prioridad_entry.grid(row=4, column=1)

        tk.Label(self.root, text="Estado:").grid(row=5, column=0)
        self.estado_entry = tk.Entry(self.root)
        self.estado_entry.grid(row=5, column=1)

        tk.Label(self.root, text="Teléfono:").grid(row=6, column=0)
        self.telefono_entry = tk.Entry(self.root)
        self.telefono_entry.grid(row=6, column=1)

        tk.Label(self.root, text="Email:").grid(row=7, column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=7, column=1)

        # Botones
        tk.Button(self.root, text="Agregar Empresa", command=self.agregar_empresa).grid(row=8, column=0, columnspan=2)
        tk.Button(self.root, text="Actualizar Tabla", command=self.actualizar_tabla).grid(row=9, column=0, columnspan=2)
        tk.Button(self.root, text="Editar Empresa", command=self.editar_empresa).grid(row=10, column=0, columnspan=2)
        tk.Button(self.root, text="Eliminar Empresa", command=self.eliminar_empresa).grid(row=11, column=0, columnspan=2)
        tk.Button(self.root, text="Exportar CSV", command=self.exportar_csv).grid(row=12, column=0, columnspan=2)

        # Cuadro de texto para mostrar la tabla
        self.tabla_text = tk.Text(self.root, height=10, width=60)
        self.tabla_text.grid(row=13, column=0, columnspan=2)

        # Permitir seleccionar una empresa para editar o eliminar
        self.tabla_text.bind("<Double-Button-1>", self.seleccionar_empresa)

    def create_database(self):
        self.conn = sqlite3.connect('empresas.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS empresas (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT,
                                industria TEXT,
                                tamaño TEXT,
                                necesidades TEXT,
                                prioridad TEXT,
                                estado TEXT,
                                telefono TEXT,
                                email TEXT)''')
        self.conn.commit()

    def agregar_empresa(self):
        nombre = self.nombre_entry.get()
        industria = self.industria_entry.get()
        tamaño = self.tamaño_entry.get()
        necesidades = self.necesidades_entry.get()
        prioridad = self.prioridad_entry.get()
        estado = self.estado_entry.get()
        telefono = self.telefono_entry.get()
        email = self.email_entry.get()

        self.cursor.execute('''INSERT INTO empresas (nombre, industria, tamaño, necesidades, prioridad, estado, telefono, email)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (nombre, industria, tamaño, necesidades, prioridad, estado, telefono, email))
        self.conn.commit()
        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.cursor.execute('''SELECT * FROM empresas''')
        empresas = self.cursor.fetchall()
        
        # Limpiar el cuadro de texto
        self.tabla_text.delete(1.0, tk.END)
        
        # Mostrar las empresas en el cuadro de texto
        for empresa in empresas:
            self.tabla_text.insert(tk.END, f"{empresa}\n")

    def seleccionar_empresa(self, event):
        # Obtener la empresa seleccionada
        index = self.tabla_text.index(tk.CURRENT)
        empresa_id = int(index.split('.')[0]) - 1
        selected_empresa = self.cursor.execute('''SELECT * FROM empresas''').fetchall()[empresa_id]
        
        # Mostrar la empresa seleccionada en los campos de entrada
        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, selected_empresa[1])
        
        self.industria_entry.delete(0, tk.END)
        self.industria_entry.insert(0, selected_empresa[2])
        
        self.tamaño_entry.delete(0, tk.END)
        self.tamaño_entry.insert(0, selected_empresa[3])
        
        self.necesidades_entry.delete(0, tk.END)
        self.necesidades_entry.insert(0, selected_empresa[4])
        
        self.prioridad_entry.delete(0, tk.END)
        self.prioridad_entry.insert(0, selected_empresa[5])
        
        self.estado_entry.delete(0, tk.END)
        self.estado_entry.insert(0, selected_empresa[6])
        
        self.telefono_entry.delete(0, tk.END)
        self.telefono_entry.insert(0, selected_empresa[7])
        
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, selected_empresa[8])

    def editar_empresa(self):
        index = self.tabla_text.index(tk.CURRENT)
        empresa_id = int(index.split('.')[0]) - 1
        selected_empresa = self.cursor.execute('''SELECT * FROM empresas''').fetchall()[empresa_id]
        
        # Obtener los nuevos datos de la empresa desde los campos de entrada
        nombre = self.nombre_entry.get()
        industria = self.industria_entry.get()
        tamaño = self.tamaño_entry.get()
        necesidades = self.necesidades_entry.get()
        prioridad = self.prioridad_entry.get()
        estado = self.estado_entry.get()
        telefono = self.telefono_entry.get()
        email = self.email_entry.get()
        
        # Actualizar la empresa en la base de datos
        self.cursor.execute('''UPDATE empresas SET nombre=?, industria=?, tamaño=?, necesidades=?, prioridad=?, estado=?, telefono=?, email=? WHERE id=?''',
                            (nombre, industria, tamaño, necesidades, prioridad, estado, telefono, email, selected_empresa[0]))
        self.conn.commit()
        self.actualizar_tabla()

    def eliminar_empresa(self):
        index = self.tabla_text.index(tk.CURRENT)
        empresa_id = int(index.split('.')[0]) - 1
        selected_empresa = self.cursor.execute('''SELECT * FROM empresas''').fetchall()[empresa_id]
        
        self.cursor.execute('''DELETE FROM empresas WHERE id=?''', (selected_empresa[0],))
        self.conn.commit()
        self.actualizar_tabla()

    def exportar_csv(self):
        self.cursor.execute('''SELECT * FROM empresas''')
        empresas = self.cursor.fetchall()
        with open('empresas.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Industria", "Tamaño", "Necesidades", "Prioridad", "Estado", "Teléfono", "Email"])
            writer.writerows(empresas)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmpresaDBApp(root)
    root.mainloop()
