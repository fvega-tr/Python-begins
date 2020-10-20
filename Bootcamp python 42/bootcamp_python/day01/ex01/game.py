class GotCharacter():

	def __init__(self, first_name, is_alive):

		self.first_name = first_name
		self.is_alive = is_alive
	

class Lannister(GotCharacter):
	'''class representing the Lannister family. Rock casterly is our home '''
	def __init__(self, first_name = None, is_alive = True):
		
		super().__init__(first_name=first_name, is_alive=is_alive)

		self.family_name = "Lannister"
		self.house_words = "A Lannister always pays his debts"

	def print_house_words(self):
		print(self.house_words)
	
	def die(self):
		self.is_alive = False

