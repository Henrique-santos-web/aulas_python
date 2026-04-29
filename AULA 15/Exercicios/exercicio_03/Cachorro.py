class Cachorro:
    def __init__(self, nome, raca):
    #* metodo __init__ é automatizar os atributos ao objeto (pesquisar melhor isso)
        self.nome = nome
        self.raca = raca

        #* self.nome/raca = atributo
        #* o que vem após o = é o que ficara dentro dos parametros da def __init__

    def ladrar(self):
        print(f"O cachorro {self.nome} da raça {self.raca} late: AU AU")


meu_cachorro = Cachorro("Rex", "Viralata")
meu_cachorro.ladrar()