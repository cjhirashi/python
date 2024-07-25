from pathlib import Path

archivo = Path('Archivos/archivo-prueba.txt')
texto = archivo.read_text()
# print(texto)

texto = archivo.read_text('utf-8').split('\n') # crea una lista de todas las líneas de texto
# print(texto2)

texto.insert(0, 'Hola Carlos')
archivo.write_text('\n'.join(texto),'utf-8')