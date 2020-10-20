from	tkinter	import	*
from	tkinter	import	filedialog

root = Tk()

def	open_file():
	filedialog.askopenfilename(title = "open", initialdir = "", filetypes = (("test" "*.py"),
	("data", "*.txt")))

Button(root, text = "open file", command = open_file).pack()

root.mainloop()