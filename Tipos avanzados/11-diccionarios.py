punto = {'x':25, 'y':50}

print(punto)

print(punto['x'])
print(punto['y'])

punto['z'] = 45

print(punto)

if 'lala' in punto:
    print('encontre lala',punto('lala'))

print(punto.get('z'))
print(punto.get('t'))
print(punto.get('t',100))

del punto['x']
del (punto['y'])

print(punto)

punto['x'] = 20

for valor in punto:
    print(valor, punto[valor])

for val in punto.items():
    print(val)
    
for llave, valor in punto.items():
    print(llave, valor)
    
usuarios = [
    {'id': 1, 'nombre': 'Carlos Jiménez'},
    {'id': 2, 'nombre': 'Isabel Paniagua'},
    {'id': 3, 'nombre': 'Ana Hirashi'},
    {'id': 4, 'nombre': 'Javier Jiménez'},
]

for usuario in usuarios:
    print(usuario['nombre'])