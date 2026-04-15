

# def informacao():
#     contagem = {}
#     info = input("Digite uma frase: ").lower

#     for caracteristicas in contagem:
#         if caracteristicas in contagem:
#             contagem[caracteristicas] = contagem[caracteristicas] + 1
#         else:
#             contagem[caracteristicas] = 1
#     return info

# informacao()
# print(contagem)

# _______________________________ essa merda não deu certo... Eu sou desprovido da inteligência? N, deve ser falta de estudo e prática

#  for caracteristicas in info:
#       if caracteristicas in info:
# * Aqui nesse for e if o IN pode significar no ou na e também "estiver no/na"

# _______________________________ Bora para a correção

def contar_caracteristica():
    print("Contador de frequencia\n")

    frase = input("Digite uma palvra: ").lower()

    contagem = {}

    for caractere in frase:

        if caractere == " ":
            continue

        if caractere in contagem:
            contagem[caractere] += 1 
        #contagem[caractere] aqui eu vou até contagem e entro no caracter (contagem é a comada e o caracter é a gaveta. O frase é uma caixa e o caracter vai olhar essa caixa e guardar nele o que vier da caixa)
        else:
            contagem[caractere] = 1

    for letra, frequencia in contagem.items():
        print(f"A letra '{letra} apareceu {frequencia} vezes")

contar_caracteristica()