from abc import ABC, abstractmethod
# Una clase abstracta no puede ser instanciada

class Model(ABC):
    @property
    @abstractmethod   
    def tabla(self):
        pass
    
    @abstractmethod
    def guardar(self):
        pass
        
    # Este método se puede ejecutar sin instanciar
    @classmethod
    def buscar_por_id(self, _id):
        print(f'buscando por id {_id} en la tabla {self.tabla}')
        
class Usuario(Model):
    tabla = 'Usuarios'
    
    def guardar(self):
        print('guardando usuario')
    
usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)