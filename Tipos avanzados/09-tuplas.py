# Una tupla no puede ser modificada, solo podemos acceder a sus datos como en las listas
numeros1 = (1,2,3)
numeros2 = (4,5,6)
numeros3 = numeros1 + numeros2

print(numeros1)
print(numeros2)
print(numeros3)

# Crear una tupla a través de cualquier elemento iterable

puntos = tuple([1,2,3,4,5,6,7,8,9])
print(puntos)