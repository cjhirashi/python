from pathlib import Path

# Cuando el programa se ejecuta en Windows (Absoluta)
# Path(r'C:\Archivos de programa\Minecraft')

# Cuando el programa se ejecuta en linux o MAC (Absoluta)
# Path('/usr/bin')

# Path()

# Ruta de origen
# Path.home()

# Ruta a archivo (Relativa)
# Path('one/__init___.py')

path = Path(r'hola-mundo\mi-archivo.py')
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name('chanchito.exe')
print(p)

p = path.with_suffix('.bat')
print(p)

p = path.with_stem('feliz')
print(p)
