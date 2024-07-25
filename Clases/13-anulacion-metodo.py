class Ave:
    def __init__(self):
        self.volador = 'Tipo volador'
        
    def vuela(self):
        print('vuela ave')
        
class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nada = 'Tipo nadador'
        
    def vuela(self):
        super().vuela()
        print('vuela pato')
        
pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)