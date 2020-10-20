from vector import *

vector1 = Vector((0, 3))
print(vector1)
vector2 = Vector(4)
print(vector2)
vector3 = Vector([1.0, 2.5, 6.0])
print(vector3)
print("Operations")
vector4 = vector1 * 5
print(vector4)
vector4 = vector1 + 5
print(vector4)
vector4 = vector1 - 5
print(vector4)
vector4 = vector1 / 2
print(vector4)
vector4 = vector1 / 0
print(vector4)

v1 = Vector(5)
v2 = Vector(5)
print(v1.__repr__())