#Obtener la cantidad de elementos mayores a 5 en la tupla.

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado = tuple(filter(lambda parameter : parameter > 5, tupla))
print(resultado)
resultado = len(resultado)
print(resultado)