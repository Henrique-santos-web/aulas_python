from SmartPhone import SmartPhone, PersonagemDeJogo, ProdutoLoja
    
smartphone1 = SmartPhone()

personagem1 = PersonagemDeJogo()

loja1 = ProdutoLoja()

if __name__ == "__main__":

    smartphone1.cor = "Preto"
    smartphone1.marca = "Motorola"
    smartphone1.botao = "volume"

    personagem1.cor = "Pardo"
    personagem1.altura = 1.73
    personagem1.habilidade = "Manipulação de Àgua"

    loja1.camiseta = "Preta"
    loja1.calca = "Azul"
    loja1.calcado = "Branco"

print(f"O celular da marca:{smartphone1.marca} e da cor:{smartphone1.cor}, quando apertado o botão {smartphone1.botao}, ele modifica o som ou tira foto caso esteja dentro da câmera\n")

print(f"O personagem é: {personagem1.cor}. \nAltura: {personagem1.altura} \nHabilidade: {personagem1.habilidade}\n")

print(f"A minha loja tem:\nCamiseta: {loja1.camiseta} \nCalça: {loja1.calca} \nCalçado: {loja1.calcado}\n")