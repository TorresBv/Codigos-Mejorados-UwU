import tkinter as tk

ventana_principal = tk.Tk()
ventana_principal.config(bg="Yellow")

def verificar_datos():
    nombre = entrada_nombre.get()
    contrasena = entrada_contrasena.get()

    if nombre == "Cpapu" and contrasena == "Basado":
        ventana_secundaria = tk.Toplevel(ventana_principal)
        ventana_secundaria.config(bg="green")
        etiqueta = tk.Label(ventana_secundaria, text="¡Bienvenido!")
        etiqueta.pack()
    else:
        etiqueta_error = tk.Label(ventana_principal, text="Nombre de usuario o contraseña incorrectos.")
        etiqueta_error.grid(row=2, columnspan=2)

etiqueta_nombre = tk.Label(ventana_principal, text="Nombre de usuario:")
etiqueta_nombre.grid(row=0, column=0)

entrada_nombre = tk.Entry(ventana_principal)
entrada_nombre.grid(row=0, column=1)

etiqueta_contrasena = tk.Label(ventana_principal, text="Contraseña:")
etiqueta_contrasena.grid(row=1, column=0)

entrada_contrasena = tk.Entry(ventana_principal, show="*")
entrada_contrasena.grid(row=1, column=1)

boton_ingresar = tk.Button(ventana_principal, text="Ingresar", command=verificar_datos)
boton_ingresar.grid(row=2, column=1)

ventana_principal.mainloop()