class Cachorro:
    def __init__(self, nome, raca):
    #* metodo __init__ é automatizar os atributos ao objeto (pesquisar melhor isso)
        self.nome = nome
        self.raca = raca 

        #* self.nome/raca = atributo
        #* o que vem após o = é o que ficara dentro dos parametros da def __init__


cachorro1 = Cachorro("Rex", "Caramelo")
print(f"{cachorro1.nome}")

#! Terminar em casa (e estudar também)

#* metodo = ação
#* atributo = o que ele tem