from tkinter import *
from tkinter import messagebox

root = Tk()

bar_menu = Menu(root)

def	information():
	messagebox.showinfo("Confirmado", "Eres una puta foca")

def	question():
	answer = messagebox.askquestion("exit", "do you want to exit?")
	
	if answer == "yes":
		root.destroy()


root.config(menu = bar_menu, width = 300, height = 300)

file_menu = Menu(bar_menu, tearoff = 0)
file_menu.add_command(label = "new file")
file_menu.add_radiobutton(label = "new window")
file_menu.add_separator()
file_menu.add_radiobutton(label = "others", command = information)
file_menu.add_radiobutton(label = "exit", command = question)

edit_menu = Menu(bar_menu)

selection_menu = Menu(bar_menu)

bar_menu.add_cascade(label = "file", menu = file_menu)

bar_menu.add_cascade(label = "edit", menu = edit_menu)

bar_menu.add_cascade(label = "selection", menu = selection_menu)

root.mainloop()