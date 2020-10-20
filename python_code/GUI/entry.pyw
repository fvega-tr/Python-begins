from tkinter import *

root = Tk()
root.title("jajejijoju")
myframe = Frame(root, width = "750", height = "500")
myframe.pack()

myname = StringVar()

#input boxes

name = Entry(myframe, textvariable = myname)
name.grid(row = 0, column = 1, pady = 10, padx = 8)
name.config(fg = "red", bg = "blue", justify = "center")

passwd = Entry(myframe)
passwd.grid(row = 1, column = 1, pady = 10, padx = 8)
passwd.config(show = "*", justify = "center")

surname = Entry(myframe)
surname.grid(row = 2, column = 1, pady = 10, padx = 8)

address = Entry(myframe)
address.grid(row = 3, column = 1, pady = 10, padx = 8)

commentary = Text(myframe, width = 50, height = 20)
commentary.grid(row = 4, column = 1, pady = 10, padx = 8)

scrollvert = Scrollbar(myframe, command = commentary.yview)
scrollvert.grid(row = 4, column = 2, pady = 10, padx = 8, sticky = NSEW)

commentary.config(yscroll = scrollvert.set)

def buttonfunction():
	myname.set("Fernando")

buttonsend = Button(myframe, text = "Send", command = buttonfunction)
buttonsend.grid(row = 5, column = 1,  pady = 10, padx = 8)

#text

name_label = Label(myframe, text = "Insert your name: ")
name_label.grid(row = 0, column = 0, sticky = "w", pady = 10, padx = 8)

passwd_label = Label(myframe, text = "Insert your password: ")
passwd_label.grid(row = 1, column = 0, sticky = "w", pady = 10, padx = 8)

surname_label = Label(myframe, text = "Insert your surname: ")
surname_label.grid(row = 2, column = 0, sticky = W, pady = 10, padx = 8)

address_label = Label(myframe, text = "Insert your address: ")
address_label.grid(row = 3, column = 0, sticky = W, pady = 10, padx = 8)

commentary_label = Label(myframe, text = "commentary: ")
commentary_label.grid(row = 4, column = 0, sticky = W, pady = 10, padx = 8)

root.mainloop()