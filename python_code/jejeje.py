lista = [["jorge", 31], ["maria", 25], ["fernando", 24]]

lista2 = [[persona[0], "mayor" if persona[1] > 30 else "menor"] for persona in lista]

#print(lista2)

students = {"claudia": {"Math": 8, "Language": 7, "English": 2},
			"Ambrosio": {"Math":9, "Language": 3, "English": 8}
		}

language = [student for student in students if students[student]["Language"] > 5]
#print(language)

c = 'a'
chars = {}
chars[c] = {}
lastchar = c

c = 'b'
chars[c] = {}
chars[lastchar][c]=1.0

print(chars)


print(chars)
