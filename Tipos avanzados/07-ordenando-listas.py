numeros = [2,6,3,7,9,10,25,48,39,4]

print(numeros)

# Ordenar lista de forma acendente

numeros.sort()
# print(numeros)

# Ordenar lista de forma decendente

numeros.sort(reverse=True)
# print(numeros)

# Ordena de forma acendente en nueva lista

numeros2 = sorted(numeros)
numeros2_invert = sorted(numeros, reverse=True)

# print(numeros)
# print(numeros2)
# print(numeros2_invert)

lista1 = [
    [2,'Isable'],
    [5,'Ana'],
    [3,'Yessica'],
    [1,'Carlos']
]

lista1.sort()
print(lista1)

# ordenar tomando como base otro elemento de la lista

lista2 = [
    ['Yessica',7],
    ['Isable',2],
    ['Ana',3],
    ['Carlos',1]
]

def ordena(elemento):
    return elemento[1]

# lista2.sort(key=ordena)

lista2.sort(key=lambda elemento:elemento[1])
print(lista2)