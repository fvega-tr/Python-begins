import datetime
from recipe import *

class Book():

	def __init__(self, name):

		self.name = name
		self.recipes_list = {"starter":[], "lunch":[], "dessert":[]}
		self.last_date = datetime.datetime.now()
		self.creation_date = datetime.datetime.now()

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for type in self.recipes_list:
			for inside in self.recipes_list[type]:
				if inside == name:
					print(inside)
					return inside
				


	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		if recipe_type in self.recipes_list:
			for recipe in self.recipes_list[recipe_type]:
				print(recipe)	

		else:
			print("recipe type not found")
		

	def add_recipe(self, recipe):
		if (not isinstance(recipe, Recipe)):
			sys.exit("The recipe must be from a Recipe class")
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = datetime.datetime.now() 
		print (recipe.name + " has been added to the Book !")
