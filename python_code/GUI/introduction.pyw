from tkinter import *

root = Tk()
root.title("me cago en rusia")
'''root.resizable(False, 1000) 
Esto es el máximo que puedes agrandar la pantalla o 
si directamente la puedes agrandar o no'''
root.geometry("750x500")
root.iconbitmap("wazowski.ico")
root.config(bg = "pink")
myframe = Frame()
myframe.pack()
'''myframe.pack(fill = "both", expand = True)
Esto es para que se expanda el frame tanto como la pantalla,
tambien estan las opciones side y anchor por ejemplo'''
myframe.config(bg = "green")
myframe.config(width = "500", height = "250")
myframe.config(relief = "groove", bd = 35)
#relief es el tipo de borde y bd el tamaño del mismo
myframe.config(cursor = "pirate")
root.mainloop()