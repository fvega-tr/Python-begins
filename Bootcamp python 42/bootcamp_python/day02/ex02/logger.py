import time
from random import randint
import logging

#logger = logging.getLogger("(fvega-tr)")
#logging.basicConfig( level=logging.DEBUG, filename= "machine.log")

logger = logging.getLogger("fvega-tr")
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler(filename="machine.log")
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('(%(name)s)%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#logging.basicConfig( level=logging.DEBUG, filename= "machine.log")
#logging.Formatter(fmt=[formato de mensaje], datefmt=[formato de fecha])

'''
logger = logging.getLogger('ejemplo_Log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.debug('mensaje debug')
logger.info('mensaje info')
logger.warning('mensaje warning')
logger.error('mensaje error')
logger.critical('mensaje critical')
'''

def log(ft_receive):
	def	ft_inside(*args, **kwargs):

		start_time = time.time()
		result = ft_receive(*args, **kwargs)
		exec_time = time.time() - start_time
		#lenght = 20 - len(ft_receive.__name__)
		if exec_time < 1:
			txt = f"Running: {ft_receive.__name__:15}"+f"[ exec-time = {exec_time:.3f} ms ]\n"
		else:
			txt = f"Running: {ft_receive.__name__:15}"+f"[ exec-time = {exec_time:.3f} s  ]\n"			
		'''fd = open("machine.log", "a")
		fd.write(txt)
		fd.close()'''
		logger.info(txt)
		return result

	return ft_inside



class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
		return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	
	machine.make_coffee()
	machine.add_water(70)