import numpy as np
from ImageProcessor import ImageProcessor

class ColorFilter():

	def invert(self, array):
		return 1 - array
	
	def blue(self, array):
		for colors in array:
			for rgb in colors:
				rgb[0] = 0
				rgb[1] = 0
		return array
	
	def green(self, array):
		for colors in array:
			for rgb in colors:
				rgb[0] = 0
				rgb[2] = 0
		return array
	
	def red(self, array):
		for colors in array:
			for rgb in colors:
				rgb[1] = 0
				rgb[2] = 0
		return array




if __name__ == "__main__":
	imagen = ImageProcessor()
	arr = imagen.load("./42AI.png")
	cf = ColorFilter()
	arr = cf.red(arr)
	imagen.display(arr)
	#print(arr)