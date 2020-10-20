class Roman:

	def __init__(self):

		self.dictionary = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
		"L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

		self.dic = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I": 1}
	
	def ord_to_roman(self, num):

		result = ""

		for key, value in self.dictionary.items():

			while num >= value:

				num -= value

				result = result + key

		return result
	
	def	roman_to_ord(self, roman_number):

		n = 0
		i = 0

		while	i < len(roman_number):

			for key, value in self.dic.items():
				
				if key == roman_number[i]:

					if (i + 1) < len(roman_number) and value < self.dic[roman_number[i + 1]]:

						n += (self.dic[roman_number[i + 1]] - value)

						i += 1

					else:

						n += value

					break
			i += 1
			
		return n


test = Roman()

print(test.ord_to_roman(124))

print(test.roman_to_ord("CXXIV"))