# frase = input("Digite a sua frase favorita: ").lower().strip()
# palavra = frase.split()

# filtro = []
# for a in palavra:
#     if len(a) > 4 and a[0] != 'a':
#         filtro.append(a)
# print(filtro)

# __________________________________________________________________________

# correção do professor a seguir...

frase = input("Digite a sua frase favorita: ").lower().strip().split(" ")

def filtrar_palavras(frase):
    palavras_filtradas = []

    for palavra in palavras_filtradas:
        if(len(palavra) > 4) and not(palavra[0] == 'a'):
            palavras_filtradas.append(palavra)

        return palavras_filtradas
    
    frase = input("Digite uma frase longa: ").lower().strip().split(" ")
    palavras_filtradas = filtrar_palavras(frase)

    # ! Terminar depois...