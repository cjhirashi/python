class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def habla(self):
        print(f'{self.nombre} dice: Guau!!!')
        
mi_perro = Perro('Rocky',2)
mi_perro.habla()