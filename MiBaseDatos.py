import tkinter as tk
import sqlite3

from tkinter import *

def login():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    if usuario == "usu" and contrasena == "cont":
        print("Inicio de sesión correcto")
    else:
        print("Nombre de usuario o contraseña incorrectos")

ventana = Tk()
ventana.geometry("300x200")
ventana.config(bg="green")
ventana.title("Inicio de sesión")

usuario_label = Label(ventana, text="Usuario:")
usuario_label.pack()

usuario_entry = Entry(ventana)
usuario_entry.pack()

contrasena_label = Label(ventana, text="Contraseña:")
contrasena_label.pack()

contrasena_entry = Entry(ventana, show="*")
contrasena_entry.pack()

boton_login = Button(ventana, text="Iniciar sesión", command=login)
boton_login.pack()

ventana.mainloop()


root = tk.Tk()
root.title("Registro de Ventas")

producto_label = tk.Label(root, text="Producto")
producto_label.grid(row=0, column=0)
producto_entry = tk.Entry(root)
producto_entry.grid(row=0, column=1)

precio_label = tk.Label(root, text="Precio")
precio_label.grid(row=1, column=0)
precio_entry = tk.Entry(root)
precio_entry.grid(row=1, column=1)

cantidad_label = tk.Label(root, text="Cantidad")
cantidad_label.grid(row=2, column=0)
cantidad_entry = tk.Entry(root)
cantidad_entry.grid(row=2, column=1)

def agregar_registro():
    
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO ventas (producto, precio, cantidad) VALUES (?, ?, ?)",
                   (producto_entry.get(), precio_entry.get(), cantidad_entry.get()))

    conexion.commit()
    conexion.close()

    producto_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)
    cantidad_entry.delete(0, tk.END)

agregar_button = tk.Button(root, text="Agregar Registro", command=agregar_registro)
agregar_button.grid(row=3, column=0, columnspan=2)


root.mainloop()

root = tk.Tk()
root.title("Registro de Ventas")

producto_label = tk.Label(root, text="Producto")
producto_label.grid(row=0, column=0)
producto_entry = tk.Entry(root)
producto_entry.grid(row=0, column=1)

precio_label = tk.Label(root, text="Precio")
precio_label.grid(row=1, column=0)
precio_entry = tk.Entry(root)
precio_entry.grid(row=1, column=1)

cantidad_label = tk.Label(root, text="Cantidad")
cantidad_label.grid(row=2, column=0)
cantidad_entry = tk.Entry(root)
cantidad_entry.grid(row=2, column=1)

def agregar_registro():
    
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO ventas (producto, precio, cantidad) VALUES (?, ?, ?)",
                   (producto_entry.get(), precio_entry.get(), cantidad_entry.get()))

    conexion.commit()
    conexion.close()

    producto_entry.delete(0, tk.END)
    precio_entry.delete(0, tk.END)
    cantidad_entry.delete(0, tk.END)

agregar_button = tk.Button(root, text="Agregar Registro", command=agregar_registro)
agregar_button.grid(row=3, column=0, columnspan=2)


root.mainloop()