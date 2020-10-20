class Hoja: 
	def __init__(self, datos, hijos=None):
		self.datos = datos
		self.hijos = None
		self.padre = None
		self.set_hijos(hijos)
	
	def __str__(self):
		return str(self.datos)

	def set_hijos(self, hijos):
		self.hijos=hijos
		if self.hijos != None:
			for h in self.hijos:
				h.padre = self

	def get_hijos(self):
		 return self.hijos

	def set_datos(self, datos):
		self.datos = datos

	def get_datos(self):
		return self.datos


def buscar_solucion():

	global solucionado
	global estado_inicial
	global solucion
	global hojas_expandidas
	global hojas_no_expandidas
	global nodo_solucion

	while (not solucionado) and len(hojas_no_expandidas)!=0:
		nodo=hojas_no_expandidas[0]
		print("nodo: ", nodo,"\n")
		hojas_expandidas.append(hojas_no_expandidas.pop(0))
		if nodo.get_datos() == solucion:
			solucionado=True
			nodo_solucion = nodo
		else:
		# expandir nodos sucesores
			dato_nodo = nodo.get_datos()
		# movimiento izquierdo
		hijo_izquierdo = Hoja([dato_nodo[1], dato_nodo[0],
		dato_nodo[2], dato_nodo[3]])
		hojas_no_expandidas.append(hijo_izquierdo)

		# movimiento central
		hijo_central = Hoja([dato_nodo[0], dato_nodo[2], dato_nodo[1],
		dato_nodo[3]])
		hojas_no_expandidas.append(hijo_central)

		# movimiento derecho
		hijo_derecho = Hoja([dato_nodo[0], dato_nodo[1], dato_nodo[3],
		dato_nodo[2]])
		hojas_no_expandidas.append(hijo_derecho)

		nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

if __name__ == "__main__":
	estado_inicial=[4,2,3,1]
	solucion=[1,2,3,4]
	hojas_expandidas=[]
	hojas_no_expandidas=[]
	solucionado=False
	nodo_solucion = None
	nodoInicial = Hoja(estado_inicial)
	hojas_no_expandidas.append(nodoInicial)
	buscar_solucion()
	# mostrar resultado (al reves)
	'''nodo=nodo_solucion
	while nodo.padre != None:
		print (nodo)
		nodo = nodo.padre

	print (nodo)'''
