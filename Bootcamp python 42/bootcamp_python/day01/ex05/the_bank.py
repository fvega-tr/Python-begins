class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount

# in the_bank.py
class Bank(object):
	"""The bank"""
	def __init__(self):
		self.account = []
	def add(self, account):
		self.account.append(account)
	def transfer(self, origin, dest, amount):
		"""
		@origin: int(id) or str(name) of the first account
		@dest: int(id) or str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		if not(isinstance(origin, Account) or isinstance(dest, Account)):
			print("source or destination account doesn't exist")
		elif amount < 0 or amount > origin.value:
			print("Amount is less than zero or amount is more than origin account value")
		elif origin.name == None or origin.id == None or origin.value == None:
			print("nombre, id or value doesn't exist")
		elif not(hasattr(origin, "^zip*") and hasattr(origin, "^addr*")) or hasattr(origin,"^b") \
		or not(hasattr(origin, "^zip*") and hasattr(origin, "^addr*")) or hasattr(origin,"^b"):
			print("Attributes must not start with b and there must be some that start with zip or addr")
		elif len(origin.__dict__) % 2 == 0 or len(dest.__dict__) % 2 == 0:
			print("The number of attributes must be even")
		else:
			return True
		
		return False
		

	def fix_account(self, account):
		"""
		fix the corrupted account
		@account: int(id) or str(name) of the account
		@return True if success, False if an error occured
		"""