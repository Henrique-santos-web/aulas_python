# def eh_maior_de_idade():
#     idade = 18

#     if idade >= 18:
#         return True
#     else:
#         return False
     
# eh_maior_de_idade()
# if eh_maior_de_idade(20):
#     print("Pode entrar")
# não tive conclusão no desafio atual

# correção professor

def eh_maior_de_idade(idade):
    if idade >= 18:
        return True
    else:
        return False

idade = int(input("Digite uma idade: "))

if eh_maior_de_idade(idade):
    print("Pode entrar!")
else:
    print("Não pode entrar!")



# Criar uma função que recebe idade não é criar dentro dela uma variavel idade = "idade que você desejar", mas sim colocar dentro dos parenteses da def(idade)
# ao colocar dentro dela a (idade), ela se torna uma variável