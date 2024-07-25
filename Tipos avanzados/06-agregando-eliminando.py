mascotas = [
    'Pelusa',
    'Pulga',
    'Diana',
    'Chanchito',
    'Firulais',
    'Solovino',
    'Diana',
    'Diana'
    ]

print(mascotas)

# Insertar en indice especifico de la lista

mascotas.insert(1,'Eliseo')
print(mascotas)

# Insertar al fina de la lista

mascotas.append('Bartolomeo')
print(mascotas)

# Eliminar la primer elemento encontrado

mascotas.remove('Diana')
print(mascotas)

# Eliminar el último elemento

mascotas.pop()
print(mascotas)

# Eliminar un elemento por el indice

mascotas.pop(1)
print(mascotas)

del mascotas[2]
print(mascotas)

# Eliminar todos los elementos de la lista

mascotas.clear()
print(mascotas)