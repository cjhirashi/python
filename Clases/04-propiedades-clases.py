class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def habla(self):
        print(f'{self.nombre} dice: Guau!!!')
        
Perro.patas = 3

mi_perro = Perro('Rocky',2)
mi_perro.habla()
print(mi_perro.patas)

mi_perro.patas = 5
print(mi_perro.patas)