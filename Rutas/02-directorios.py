from pathlib import Path

path = Path('Rutas')
# path.exists() # Comprueba si existe el directorio
# path.mkdir() # Crea el directorio
# path.rmdir() # Remueve el directorio, solo si se encuentra vacio
# path.rename('nuevo_nombre') # Cambia el nombre del directorio

for p in path.iterdir():
    print(p)
    
archivos = [p for p in path.iterdir() if not p.is_dir()]

print(archivos)

archivos2 = [p for p in path.glob('*.py')]
print(archivos2)

# archivos2 = [p for p in path.glob('01-*.py')]
# archivos2 = [p for p in path.glob('**\*.py')]
# archivos2 = [p for p in path.rglob('*.py')]