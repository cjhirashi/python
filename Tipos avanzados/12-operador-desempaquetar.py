lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
combinada = ['hola',*lista1,'mundo', *lista2]

print(combinada)

punto1 = {'x': 19}
punto2 = {'y': 16}

nuevoPunto = {**punto1,**punto2,'z':10}

print(nuevoPunto)