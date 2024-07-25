mensaje = 'Bienvenido'

def saludar(nombre):
    global mensaje
    print(f'{mensaje}: {nombre}')
    
saludar('Carlos')