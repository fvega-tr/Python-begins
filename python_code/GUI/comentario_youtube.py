
"""Ventana que puede recoger los datos de un cliente."""

from tkinter import *


def recogerDatos():
    print(nombre.get(), apellido.get(), contrasena.get(), direccion.get())


raiz = Tk()

nombre = StringVar()
apellido = StringVar()
contrasena = StringVar()
direccion = StringVar()


# Ventana principal:
miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

# Cuadro del nombre:

cuadroNombre = Entry(miFrame, textvariable=nombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)

# Cuadro del apellido:

cuadroApellido = Entry(miFrame, textvariable=apellido)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)

# Cuadro de la contraseña:
cuadroPass = Entry(miFrame, textvariable=contrasena)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

# Cuadro de la dirección:

cuadroDireccion = Entry(miFrame, textvariable=direccion)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

# Cuadro de texto:
textoComentario = Text(miFrame, width=16, height=10)
textoComentario.grid(row=4, column=1, padx=10, pady=10)

# Scroll del texto:
scrollVertical = Scrollbar(miFrame, command=textoComentario.yview)
scrollVertical.grid(row=4, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVertical.set)

# Label del nombre:
nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

# Label del apellido:
apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

# Label de la contraseña:
passLabel = Label(miFrame, text="Contraseña: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

# Label de dirección:
direccionLabel = Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

# Botón:
botonEnvio = Button(raiz, text="Enviar", command=recogerDatos)
botonEnvio.pack()


raiz.mainloop()