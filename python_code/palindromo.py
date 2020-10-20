palindromo = input("Introduce una palabra\n")
j = 1
for i in palindromo:
    if (i == palindromo[-j]):
        ispa = True
        j += 1
    else:
        ispa = False
        break
if ispa:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")