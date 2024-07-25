class Perro:
    def __init__(self, nombre):
        self.set_nombre(nombre)
    
    @property    
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def set_nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
            