class Produto:
    def __init__(self, nome, preco, estoque):

        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print("Venda realizada")
        else:
            print("Estoque insuficiente")