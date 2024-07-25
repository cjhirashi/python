# Todos los métodos mágicos su nombre se establece como __nombre__ con dos guiones bajos al inicio y dos al final

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __del__(self):
        print(f'Elemento Perro <{self.nombre}> eliminado...')
        
    def __str__(self):
        return f'<Clase Perro: {self.nombre}>'
        
    def habla(self):
        print(f'{self.nombre} dice: Guau!!!')
        
perro = Perro('Rocky',4)
print(perro)

texto = str(perro)
print(texto)

del perro