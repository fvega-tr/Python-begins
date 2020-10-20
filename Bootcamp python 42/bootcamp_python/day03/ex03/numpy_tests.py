import numpy as np

#creamos un array de 0 o de 1
# si en el primer parametro le pasamos una lista podemos hacer una matriz
#el primero de la lista seran filas, el segundo columnas y si le pasamos un tercero
#sera el numero de dimensiones de este es decir las caras
array = np.zeros(10)
print(array)

array2 = np.ones((10, 10, 10))
print(array2)

#array con 10 numeros 7
array3 = np.ones(10) * 7
print(array3)

#para obtener informacion dentro de info metemos la funcion que queramos
np.info()

# comprobar si alguno de los elementos es igual a cero, devuelve true or false

np.all(array)

# comprobar si alguno de los elementos es distinto de cero, devuelve true or false

np.any(array)

#array rango entre 20 y 50
a = np.arange(20, 50)
print(a)

#array rango entre 20 y 50 solo los pares
a = np.arange(20, 50, 2)
print(a)

#crear una matriz identidad
matriz = np.identity(3)
print(matriz)

#crear tambien una matriz identidad

identidad = np.eye(5)

#tambien para crear una matriz reshape cambia de forma
#por ejemplo para cambiar de un array a una matriz
print(np.arange(2, 20).reshape(3, 6))

#imprimir una matriz elemento a elemento

for i in np.nditer(matriz):
	print(i)

#Crear un Arreglo con 5 Valores Distribuidos Uniformemente entre 10 y 50

array4 = np.linspace(10, 50, 5)
print(array4)

#Crear un Arreglo con Valores 0 a 9, e Invertir el Signo de los Valores 5 a 7

arreglo = np.arange(10)
arreglo[(arreglo >= 5) & (arreglo <= 7)] *= -1

#calcular el numero de filas y columnas de una matriz
print(matriz.shape)


#cambiarle todos los numero menos el marco a una matriz

marco = np.zeros((5, 5))
marco[1:-1, 1:-1] = 1
print(marco)

#escalonar ceros y unos en una matriz

escalonar = np.zeros((5, 5))
escalonar[::2, ::2] = 1
escalonar[1::2, 1::2] = 1
print(escalonar)

#para sumar una matriz

suma = np.random.random((5, 5))
print(suma)
print("{0:.3f}".format(np.sum(suma)))

#para sumarla por columnas axis = 0
print(np.sum(suma, axis = 0))

#para sumarla por filas axis = 1
print(np.sum(suma, axis = 1))

#Calcular el Producto Punto entre Dos Vectores
a = np.array([2, 3])
b = np.array([1, 5])
print(np.dot(a, b))

#Sumar un Arreglo a Cada Fila de una Matriz

a = np.array([1,1,1])
b = np.array([[1,1,1], [2,2,2]])
for i in b:
	print(i + a)


#crear una grafica

import matplotlib.pyplot as plt

x = np.arange(-5, 5)
y = np.arange(-5, 5)

#plt.plot(x, y)
#plt.show()


prueba = np.full(6, 2)
print(prueba)

#multiplicacion, division y suma de escalares

#np.add(1, 2) para sumar

#np.subtract(1, 2) para restar

#np.multiply(1, 2) para multiplicar

#np.divide
