from Forma import Forma

class Quadrado(Forma):
    
    def __init__(self, lado):
        self.lado = lado #* Entender melhor por que tive que fazer assim

    def calcular_area(self):
        return self.lado * self.lado