mascotas = {'gato': {'Maria', 'Luis'},
'perro': {'Maria', 'Karen', 'Ana'},
'rana':set(),
'conejo': {'Maria', 'Karen', 'Juan'}}

test = (mascotas['perro'] & mascotas['conejo']) - mascotas['gato']
print(test)

mascotas['rana'] = "pollas"
print(mascotas)


var = list("ba127342b598d6ea5aba28109bc8dc57")
var2 = []
for i in var:
	if i not in var2:
		var2.append(i)
		print(i, end= ' ')
