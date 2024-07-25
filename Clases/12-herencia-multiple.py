class Animal:
    
    def comer(self):
        print('comiendo')

class Perro:
    
    def pasear(self):
        print('paseando')
        
class Chanchito(Perro, Animal): 
     
    def programar(self):
        print('programando')
        
perro = Perro()
perro.pasear()

print('chanchito')
chanchito = Chanchito()
chanchito.comer()
chanchito.pasear()
chanchito.programar()