from tkinter import *

root = Tk()
my_frame = Frame(root, width = "750", height = "500")

my_frame.pack()
my_image = PhotoImage(file = "homer.gif")
#se puede abreviar de la siguiente manera
#Label(my_frame, text = "hola hola").place(x = "100", y = "100")
#my_label = Label(my_frame, text = "hola hola", font = ("Comic Sans MS", 50), fg = "#009100")
#my_label.place(x = "100", y = "100")
Label(my_frame, image = my_image).place(x = "100", y = "100")
root.mainloop()