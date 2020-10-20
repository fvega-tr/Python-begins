manejador = open("filepython.txt", 'r')
texto = manejador.read()
palabras = texto.split()
contadores = dict()
for palabra in palabras:
	contadores[palabra] = contadores.get(palabra,0) + 1
mayorcantidad = None
mayorpalabra = None
for palabra,contador in contadores.items():
	if mayorcantidad is None or contador > mayorcantidad:
		mayorpalabra = palabra
		mayorcantidad = contador
print(mayorpalabra, mayorcantidad)