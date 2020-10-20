import sys
import time

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	if isinstance(text, str) == False:
		sys.exit("The text must be a string")

	if option != None:
		option = option.lower()
		if option != "shuffle" and option != "unique" and option != "ordered":
			sys.exit("Option not valid")

	text = text.split(sep)

	if option == "shuffle":
		shuffle = int(time.strftime("%S"))
		shuffle *= len(text[len(text) - int(len(text)/2)])
		i = shuffle
		while i > 0:
			shuffle = int(time.strftime("%S"))
			shuffle = int(shuffle / i)
			if shuffle < len(text):
				swap = text[shuffle]
				text[shuffle] = text[0]
				text[0] = swap
			i -= 1

	if option == "ordered":
		text.sort()
	
	if option == "unique":
		text = set(text)
	
	for i in text:
		yield i
	
for i in generator("hola que pasa manolo tejon hola que loco", sep=" ", option="shuffle"):
	print(i)