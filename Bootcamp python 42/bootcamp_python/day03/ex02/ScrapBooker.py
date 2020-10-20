import numpy as np
import matplotlib.pyplot as plt
import sys
from ImageProcessor import ImageProcessor

class ScrapBooker():

	def crop(self, array, dimensions, position=(0, 0)):

		if (dimensions[0] + position[0]) > array.shape[0] or \
		dimensions[1]  + position[1] > array.shape[1]:
			sys.exit("Error: the cropping can't be greater than the array")

		return	array[position[0]: position[0] + dimensions[0], position[1]: position[1] + dimensions[1]]

	def thin(self, array, n, axis):
		
		if axis == 0:
			return array[::n, :]
		else:
			return array[: , ::n]
		
	def juxtapose(self, array, n, axis):
		if axis == 0:
			return np.tile(array, (n, 1))
		else:
			return np.tile(array, (1, n))
	
	def mosaic(self, array, dimensions):
		return np.tile(array, dimensions)



img = ImageProcessor()
booker = ScrapBooker()
arr = img.load("./42AI.png")
#arr = booker.crop(arr, (150, 150))
#arr = booker.thin(arr, 50, 0)
img.display(arr)