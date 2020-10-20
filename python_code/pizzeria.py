untouchables = ("mozzarella", "tomato")
print("Do you want a vegetarian pizza?")
answer = input()
answer = answer.lower()
if answer == "yes":
	print("Choose one ingredient between tofu or pepper")
	ingredient = input()
	vegetarian = True
else:
	print("Choose one ingredient between tofu, pepper, ham, pepperoni and salmon")
	ingredient = input()
	vegetarian = False
if vegetarian:
	print("The pizza is vegetarian and has a following ingredient: " + untouchables[0] + untouchables[1] + ingredient)
else:
	print("The pizza isn't vegetarian and has a following ingredient: " , untouchables[0] , untouchables[1] ,ingredient, sep = ", ", end = ".")