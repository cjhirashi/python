# Las propiedades privadas no pueden ser modificadas una vez creada la instancia, solo se podrá acceder
# a esas variables a través de un método, se puede modificar solo a través de un método

class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def habla(self):
        print(f'{self.__nombre} dice: Guau!!!')
        
    @classmethod
    def factory(cls):
        return cls('Rocky', 4)
        
mi_perro = Perro('Rocky',4)

mi_perro.habla()

print(mi_perro.get_nombre())

