import sys

argc = len(sys.argv)
str2 = ""

morse_code = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--.."}

if argc != 2:
	print("usage: ./xlogin.py <a-zA-Z string>")

else:
	try:
		string = sys.argv[1].lower()
		for i in string:
				str2 += morse_code[i]
				
		print(str2)
	except:
		print("usage: ./xlogin.py <a-zA-Z string>")