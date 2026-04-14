# def cadastrar_usuario():

#     while True:
#         try:
#             idade_usuario = int(input("Qual a sua idade? "))

#             if idade_usuario < 0 or idade_usuario > 120:
#                 print("Idade inválida")
#                 continue
#             else:
#                 break
#         except ValueError:
#             print("Digite apenas números!")

#     while True:
#         try:
#             nome_usuario = input("Qual o seu nome? ").strip()

#             break
#         except:
#             print("Encerrando o crachá...")
#             continue

#     return {"nome" : nome_usuario, "idade" : idade_usuario}

# cadastro = cadastrar_usuario()

# print(f"O seu cadastro: {cadastro}")


# *o return não pode ficar dentro do while
# * se não o primeiro breack já cancela o return e a informação nunca chegará à variável cadastro
# * assim impedindo o print com o resultado!

# _____________________________________________

# correção do professor

def cadastrar_usuario():
    while True:
        try:
            idade = int(input("Digite sua idade"))

            if idade < 0 or idade > 120:
                print("Idade inválida")
                continue #caso a idade seja válida, o continue dará continuidade

            break

        except ValueError:
            print("Erro: Idade deve ser um número inteiro.")

    nome_usuario = input("Digite o nome do usuario: ")

    return{
        "nome" : nome_usuario,
        "idade" : idade
    }

print(cadastrar_usuario())