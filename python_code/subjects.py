subjects = ["math", "lenguage", "history", "physical", "chemistry"]
for subject in subjects:
	change = int(input(f"What is your note in {subject}\n"))
	test = subject
	if change > 4:
		subjects.remove(test)
	print (subject)
print(subjects)