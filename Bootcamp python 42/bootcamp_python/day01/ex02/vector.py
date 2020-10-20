import sys

class Vector():

	def __init__(self, values):

		if isinstance(values, int):
			self.values = []
			for i in range(values):
				self.values.append(i)
		
		elif isinstance(values, tuple):
			self.values = []
			for i in range(values[0], values[1]):
				self.values.append(float(i))

		else:
			self.values = values

		if isinstance(values, int) == False:
			self.len = len(values)

	def	__add__(self, n):

		res = []
		if isinstance(n, int) == False:
			for i in range(self.len):
				res.append(self.values[i] + n[i])
		else:
			res = [i + n for i in self.values]

		return Vector(res)
	
	def __radd__(self, n):

		res = []
		if isinstance(n, int) == False:
			for i in range(self.len):
				res.append(self.values[i] + n[i])
		else:
			res = [i + n for i in self.values]

		return Vector(res)
	
	def __sub__(self, n):

		res = []
		if isinstance(n, int) == False:
			for i in range(self.len):
				res.append(self.values[i] - n[i])
		else:
			res = [i - n for i in self.values]
		
		return Vector(res)
		
	def __rsub__(self, n):

		res = []
		if isinstance(n, int) == False:
			for i in range(self.len):
				res.append(self.values[i] - n[i])
		else:
			res = [i - n for i in self.values]
		
		return Vector(res)
	
	def __truediv__(self, n):

		if (n == 0):
			sys.exit("Can't divide by 0")
		res = []
		if isinstance(n, int) == False:
			for i in range(self.len):
				res.append(self.values[i] / n[i])
		else:
			res = [i / n for i in self.values]
		
		return Vector(res)

	def __rtruediv__(self, n):

		if (n == 0):
			sys.exit("Can't divide by 0")
		res = []
		if isinstance(n, int) == False:
			for i in range(self.len):
				res.append(self.values[i] / n[i])
		else:
			res = [i / n for i in self.values]
		
		return Vector(res)
	
	def __mul__(self, n):

		res = []
		if isinstance(n, int) == False:
			for i in range(self.len):
				res.append(self.values[i] * n[i])
		else:
			res = [i * n for i in self.values]
		
		return Vector(res)

	def __rmul__(self, n):

		res = []
		if isinstance(n, int) == False:
			for i in range(self.len):
				res.append(self.values[i] * n[i])
		else:
			res = [i * n for i in self.values]
		
		return Vector(res)
	

	def __str__(self):

		text = "Vector " + str(self.values)
		return (text)
	
	def __repr__(self):

		return "%s(%r)" % (self.__class__, self.__dict__)
