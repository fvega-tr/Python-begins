fruits = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruit = input('¿Qué fruta quieres? ')
kg = float(input('¿Cuántos kilos? '))
try:
	print("El precio de " + fruit + " es de " + str(kg * fruits[fruit]))
except:
	print("Esa fruta no se encuentra disponible juan julian")