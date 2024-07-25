class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # Este método se puede ejecutar sin instanciar la clase
    @classmethod
    def habla(cls):
        print('Guau!!!')
       
    # Este método se puede ejecutar sin instanciar la clase 
    @classmethod
    def factory(cls):
        return cls('Rocky', 4)
        
Perro.habla()

perro1 = Perro('Lennon',4)
perro2 = Perro('Zeus',3)
perro3 = Perro.factory()

print(perro3.nombre,perro3.edad)