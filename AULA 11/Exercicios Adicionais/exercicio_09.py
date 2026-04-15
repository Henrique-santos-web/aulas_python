# print("Crie uma senha forte!\nEla deve conter:")
# print("8 caracteres")

# def validar_senha(senha):
#     input("Nova senha: ") 
#     while True:
#         if len(senha) == 8:
#             print("Senha forte!")
#             senha = True
#             break
#         else:
#             print("Senha fraca!!")
#             print("Tente novamente")
#             continue
#     return senha
# validar_senha()

# novamente deu errado, mas sem desistir

# _____________________________________

# correção do professor

def validar_senha(senha):
    if len(senha) < 8:
        return False
    
    if not any(char.isdigit() for char in senha):
        return False

    if not any(char.isupper() for char in senha):
        return False

    if not any(char.islower() for char in senha):
        return False
    
    return True

print("Regras: Minimo 8 caracteres, 1 numero, 1 maiusculo, 1 minusculo")
usuario_senha = input("Digite a senha nova: ")

if validar_senha(usuario_senha):
    print("Senha forte")
else:
    print("Senha fraca")
    