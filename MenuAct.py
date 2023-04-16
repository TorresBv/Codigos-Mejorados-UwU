import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.config(bg="blue")

def abrir_archivo():
    archivo = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo is not None:
        contenido = archivo.read()
        print(contenido)
        archivo.close()

def guardar_archivo():
    archivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo is not None:
        archivo.write("¡Hola, mundo!")
        archivo.close()

menu = tk.Menu(root)
root.config(menu=menu)

archivo_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Abrir archivo", command=abrir_archivo)
archivo_menu.add_command(label="Guardar archivo", command=guardar_archivo)

root.mainloop()
