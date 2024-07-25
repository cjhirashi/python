numeros = [1,2,3,4,5,6,7,8,9]

print(numeros)

# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[3]

primero, segundo, tercero, *mas = numeros

print(primero)
print(segundo)
print(tercero)

primer, dos, *otros, ultimo = numeros

print(primer)
print(dos)
print(otros)
print(ultimo)