import tkinter as tk
import sqlite3

class VentanaMenu:
    def __init__(self, master):
        self.master = master
        master.title("Menú principal")
        master.config(bg="Green")

        self.agregar_alumnos_button = tk.Button(master, text="Agregar alumno", command=self.abrir_ventana_agregar_alumnos)
        self.agregar_alumnos_button.pack()

        self.salir_button = tk.Button(master, text="Salir", command=master.quit)
        self.salir_button.pack()
    
    def abrir_ventana_agregar_alumnos(self):
        self.ventana_agregar_alumnos = tk.Toplevel(self.master)
        self.app_agregar_alumnos = VentanaAgregarAlumnos(self.ventana_agregar_alumnos)

class VentanaAgregarAlumnos:
    def __init__(self, master):
        self.master = master
        master.title("Agregar alumno")
        
        self.nombre_label = tk.Label(master, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(master)
        self.nombre_entry.pack()

        self.edad_label = tk.Label(master, text="Edad:")
        self.edad_label.pack()
        self.edad_entry = tk.Entry(master)
        self.edad_entry.pack()

        self.guardar_button = tk.Button(master, text="Guardar", command=self.guardar_alumno)
        self.guardar_button.pack()

    def guardar_alumno(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()

        conn = sqlite3.connect('estudiantes.db')
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS alumnos (nombre text, edad integer)")
        c.execute("INSERT INTO alumnos VALUES (?, ?)", (nombre, edad))

        conn.commit()
        conn.close()

        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = VentanaMenu(root)
    root.mainloop()
