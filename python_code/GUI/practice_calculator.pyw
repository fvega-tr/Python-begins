from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)
myframe = Frame(root, cursor = "hand2")
myframe.pack()

operation = ""
last_operation = ""
result = 0
number = StringVar()


#entry

screen = Entry(myframe, textvariable = number)
screen.grid(row = 1, column = 1, padx = 3, pady = 3, columnspan = 4)
screen.config(fg = "green", bg = "black", justify = "center")

#functions

def	pressnumber(num):
	global operation

	if operation != "":
		number.set(num)
		operation = ""
	else:
		number.set(number.get() + num)


def	ft_suma(num):
	global operation
	global result
	global last_operation
	if operation == "":
		result += int(num)
	operation = "+"
	last_operation = "+"
	number.set(result)

def ft_minus(num):
	global operation
	global result
	global last_operation
	if result != 0 and operation != "-":
		result -= int(num)
	elif result == 0 and operation != "-":
		result = int(num)
	operation = "-"
	last_operation = "-"
	number.set(result)


def ft_equal(num):
	global result
	global operation
	global last_operation

	if last_operation == "+" and operation == "":
		result += int(num)
	elif last_operation == "-" and operation == "":
		result -= int(num)
	operation = "="
	last_operation = "="
	number.set(result)

#buttons

#-------------1ª row--------------------------

seven = Button(myframe, text = "7", width = 3, command = lambda:pressnumber("7"))
seven.grid(row = 2, column = 1, padx = 3, pady = 3)

eight = Button(myframe, text = "8", width = 3, command = lambda:pressnumber("8"))
eight.grid(row = 2, column = 2, padx = 3, pady = 3)

nine = Button(myframe, text = "9", width = 3, command = lambda:pressnumber("9"))
nine.grid(row = 2, column = 3, padx = 3, pady = 3)

div = Button(myframe, text = "/", width = 3)
div.grid(row = 2, column = 4, padx = 3, pady = 3)

#-------------2ª row--------------------------

four = Button(myframe, text = "4", width = 3, command = lambda:pressnumber("4"))
four.grid(row = 3, column = 1, padx = 3, pady = 3)

five = Button(myframe, text = "5", width = 3, command = lambda:pressnumber("5"))
five.grid(row = 3, column = 2, padx = 3, pady = 3)

six = Button(myframe, text = "6", width = 3, command = lambda:pressnumber("6"))
six.grid(row = 3, column = 3, padx = 3, pady = 3)

mult = Button(myframe, text = "X", width = 3)
mult.grid(row = 3, column = 4, padx = 3, pady = 3)

#-------------3ª row--------------------------

one = Button(myframe, text = "1", width = 3, command = lambda:pressnumber("1"))
one.grid(row = 4, column = 1, padx = 3, pady = 3)

two = Button(myframe, text = "2", width = 3, command = lambda:pressnumber("2"))
two.grid(row = 4, column = 2, padx = 3, pady = 3)

three = Button(myframe, text = "3", width = 3, command = lambda:pressnumber("3"))
three.grid(row = 4, column = 3, padx = 3, pady = 3)

minus = Button(myframe, text = "-", width = 3, command = lambda:ft_minus(number.get()))
minus.grid(row = 4, column = 4, padx = 3, pady = 3)

#-------------4ª row--------------------------

zero = Button(myframe, text = "0", width = 3, command = lambda:pressnumber("0"))
zero.grid(row = 5, column = 1, padx = 3, pady = 3)

equal = Button(myframe, text = "=", width = 3, command = lambda:ft_equal(int(number.get())))
equal.grid(row = 5, column = 2, padx = 3, pady = 3)

point = Button(myframe, text = ".", width = 3)
point.grid(row = 5, column = 3, padx = 3, pady = 3)

suma = Button(myframe, text = "+", width = 3, command = lambda:ft_suma(int(number.get())))
suma.grid(row = 5, column = 4, padx = 3, pady = 3)

root.mainloop()