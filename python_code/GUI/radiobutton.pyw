from tkinter import *

root = Tk()

option = IntVar()

def	ft():
	if option.get() == 1:
		ft_label.config(text = "You have chosen: yes")
	if option.get() == 2:
		ft_label.config(text = "You have chosen: no")


Label(root, text = "do you agree?").pack()
Radiobutton(root, text = "yes", Variable = option, value = 1, command = ft).pack()
Radiobutton(root, text = "no", Variable = option, value = 2, command = ft).pack()

ft_label = Label(root).pack()

root.mainloop()