class Animal:
    def __init__(self, nome):
        self.nome = nome

    
    def comer(self):
        print(f"O {self.nome} está comendo." )


    def emitir_som(self):
        print("Som indefinido")