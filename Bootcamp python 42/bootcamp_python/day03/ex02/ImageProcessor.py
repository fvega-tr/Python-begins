import numpy as np
import matplotlib.pyplot as plt

class ImageProcessor():

	def	load(self, path):
		img = plt.imread(path)
		print(f"Loading image {img.shape[0]} X {img.shape[1]}")
		return img

	def	display(self, array):
		plt.imshow(array)
		plt.show()

#imagen = ImageProcessor()
#arr = imagen.load("./42AI.png")
#imagen.display(arr)
