import string

def text_analyzer(text = None):
	''' This function counts the number of upper characters, lower characters,
		punctuation and spaces in a given text. '''
	if text == None:
		text = input("What is the text to analyze ?\n")
		
	while (len(text) == 0):
		text = input("What is the text to analyze ?\n")
	print("The text contains", len(text) ,"characters:")
	print("-", sum(map(str.islower, text)), "lower letters")
	print("-", sum(map(str.isupper, text)), "upper letters")
	print("-", sum((map(lambda char: char in string.punctuation , text))), "punctuations")
	print("-", len(text.split(" ")), "spaces")
