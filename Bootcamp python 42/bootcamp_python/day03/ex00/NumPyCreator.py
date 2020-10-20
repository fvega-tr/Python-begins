import numpy as np

class NumPyCreator():
	
	def	from_list(self, lst, type=None):
		return np.array(lst, dtype=type)
	
	def from_tuple(self, tp, type=None):
		return np.array(tp, dtype=type)

	def	from_iterable(self, iter, type=None):
		return np.array(iter, dtype=type)
	
	def from_shape(self, shape, fill_value=0, type=None):
		return np.full(shape, fill_value, dtype=type)
		#return	np.array.ones(shape, dtype=type) * number

	def random(self, shape):
		return np.random.random(shape)
	
	def	identity(self, shape, type=None):
		return np.identity(shape)

	
