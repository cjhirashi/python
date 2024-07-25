usuarios = [
    ['Yessica',7],
    ['Isable',2],
    ['Ana',3],
    ['Carlos',1]
]

# nombres=[]
# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

# Transformar elementos (comprención de listas)

nombres = [usuario[0] for usuario in usuarios]

print(nombres)

# Filtrar elementos (comprención de listas)

nombres2 = [usuario for usuario in usuarios if usuario[1] > 2]

print(nombres2)

# Filtrar y transformar elementos (comprención de listas)

nombres3 = [usuario[0] for usuario in usuarios if usuario[1] > 2]

print(nombres3)

# Transforma con map

nombres4 = list(map(lambda usuario: usuario[0], usuarios))

print(nombres4)

# Filtar con filter

nombres5 = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(nombres5)