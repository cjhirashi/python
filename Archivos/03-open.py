from io import open

# Escritura
# texto = 'Hola Carlos!!!'

# archivo = open('Archivos/hola.txt', 'w') # Se abre en modo escritura
# archivo.write(texto)
# archivo.close()

# Lectura
# archivo = open('Archivos/hola.txt', 'r')
# texto = archivo.read()
# archivo.close()
# print(texto)

# Lectura como lista
# archivo = open('Archivos/hola.txt', 'r')
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# With y Seek
# with open('Archivos/hola.txt', 'r') as archivo:
#     print(archivo.readlines())
    
#     archivo.seek(0) # Esta instrucción hace que el puntero se valla a un caracter en específico
    
#     for linea in archivo:
#         print(linea)
        
# Agregar
# archivo = open('Archivos/hola.txt', 'a+')
# archivo.write('Chao mundo!!!')
# archivo.close()

# Lectura y escritura
with open('Archivos/hola.txt', 'r+') as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = 'Chanchito Feliz'
    print(texto)
    archivo.writelines(texto)