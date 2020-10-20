dictionary = {"nombre": "", "edad": "", "telefono": ""}
data = []
hola3 = (input("Introduce nombre"))
hola1= (input("Introduce un numero"))
hola2= (input("Introduce un telefono"))
data = hola3, hola1, hola2
dictionary["nombre"] = data[0]
dictionary["edad"] = data[1]
dictionary["telefono"] = data[2]
print(dictionary)