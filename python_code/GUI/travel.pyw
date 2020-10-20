from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

falete = IntVar()
ballena = IntVar()

def	joder():
	option = ""
	if falete.get() == 1:
		option += "falete a tu lado parece que acaba de salir de un campo de concentración"
	elif ballena.get() == 1:
		option += "no insultes a las putas ballenas gordo cabrón"
	final_msg.config(text = option)

homer = PhotoImage(file = "homer.gif")
Label(frame, image = homer).pack()

Label(frame, text = "Tu estado físico esta cuarentena es:", width = 50).pack()
Checkbutton(frame, text = "Ni falete en sus mejores tiempos", variable = falete, onvalue = 1, offvalue = 0, command = joder).pack()
Checkbutton(frame, text = "Una puta ballena", variable = ballena, onvalue = 1, offvalue = 0, command = joder).pack()

final_msg = Label(frame)
final_msg.pack()

root.mainloop()