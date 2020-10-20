import sys

class Recipe:

	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		
		if len(name) == 0 or isinstance(name, str) != True:
			sys.exit("Name Error: The name can't be empty and must be of type str")
		self.name = name
		
		if isinstance(cooking_lvl, int) != True or cooking_lvl == 0:
			sys.exit("Cooking_lvl Error: The cooking_lvl can't be empty and must be of type integer")
		self.cooking_lvl = cooking_lvl
		
		if isinstance(cooking_time, int) != True or cooking_time == 0:
			sys.exit("Cooking_timecooking_time Error: The cooking_time can't be empty and must be of type integer")
		self.cooking_time = cooking_time

		if len(ingredients) == 0 or isinstance(ingredients, list) != True:
			sys.exit("Ingredients Error: The ingredients can't be empty and must be of type list")
		self.ingredients = ingredients

		self.description = description

		recipe_type = recipe_type.lower()

		if len(recipe_type) == 0 or isinstance(recipe_type, str) != True or (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
			sys.exit("Recipe type Error: The recipe can't be empty and must be can be “starter”, “lunch” or “dessert”.")
		self.recipe_type = recipe_type

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = ""
		txt += "Name: " + self.name + "\n"
		txt += "Cooking lvl: " + str(self.cooking_lvl) + "\n"
		txt += "Cooking time " + str(self.cooking_time) + "\n"
		txt += "Ingredients:"
		for ingredient in self.ingredients:
			txt += " " + ingredient
		txt += "\n"
		txt += "Description: " + self.description + "\n"
		txt += "Recipe type: " + self.recipe_type + "\n"
		return txt

