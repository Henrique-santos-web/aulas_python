class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def sofrer_dano(self, dano):
        self.vida -= dano
        return f"Você sofreu {dano} de dano. Status de HP: {self.vida}"

guerreiro = Guerreiro("Pedro")
print(guerreiro.sofrer_dano(20))