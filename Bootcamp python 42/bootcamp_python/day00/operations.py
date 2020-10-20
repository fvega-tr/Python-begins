import sys

if len(sys.argv) > 3:
	print("Input error:   too many arguments")
	sys.exit("Usage: python operations.py <number1> <number2> \nExample: python operations.py 10 3")

if len(sys.argv) < 3:
    sys.exit("Usage: python operations.py <number1> <number2> \nExample: python operations.py 10 3")

if sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
	print("Input error:   only number")
	sys.exit("Usage: python operations.py <number1> <number2> \nExample: python operations.py 10 3")


num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum :            "+str(num1 + num2))
print("Difference :     "+str(num1 - num2))
print("Product :        "+str(num1 * num2))
if (num2 != 0):
    print("Quotient :       "+str(num1 / num2))
    print("Remainder :      "+str(num1 % num2))
else:
    print("Quotient :       "+ "Error  (div by zero")
    print("Remainder :      "+ "Error (modulo by zero")