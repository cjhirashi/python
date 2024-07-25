from pathlib import Path
from time import ctime

archivo = Path('Archivos/archivo-prueba.txt')
# archivo.exists() # Existe el archivo
# archivo.rename() # Renombrar el archivo
# archivo.unlink() # Eliminar el archivo

print(archivo.stat())
print(' fecha acceso: ', ctime(archivo.stat().st_atime))
print(' fecha creación: ', ctime(archivo.stat().st_ctime))
print(' fecha modificación: ', ctime(archivo.stat().st_mtime))