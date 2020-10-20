invoices = {}
total = 0
answer = ""
while answer != "end":
	key = input("Introduce el numero de factura\n")
	value = input("Introduce el valor de la factura\n")
	invoices.setdefault(key, value)
	answer = input("What do you want do you now? end, delete o continue\n")
	while answer == "delete":
		number = input("Insert the number of invoice\n")
		if number in invoices:
			total += int(invoices[number])
			del invoices[number]
		answer = input("What do you want do you now? end, delete o continue\n")
print("The sum of the settled amount is: " + str(total))
	