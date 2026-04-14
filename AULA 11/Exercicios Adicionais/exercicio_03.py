# extrato = []

# saldo = float(1000.00)


# while True:

#     opcao = (input("Escolha uma das opções abaixo: \n1- Sacar\n2- Depositar\n3- Ver Saldo\n4- Sair\n"))

#     match opcao:
#         case "1":
#             saque = float(input("Quanto o senhor deseja sacar? "))
#             if saque > saldo :
#                 print("Saldo insuficiente!")
#             elif saque <= saldo:
#                 saldo -= saque
#                 extrato.append("Saque", saldo)
#                 print(f"Saque no valor de R${saque} realizado com sucesso.\nSeu saldo atual é de: R${saldo}")
#             else:
#                 print("ERRO")
#         case "2":
#             depositar = float(input("Quanto deseja depositar? "))
#             if depositar > 0:
#                 saldo += depositar
#                 extrato.append(("Deposito", depositar))
#                 print("Depósito realizado com sucesso!")
#             else:
#                 print("Erro! Digite um valor positivo...")
#         case "3":
#             print(f"Seu saldo é de: R${saldo:.2f}")
#         case "4":
#             if not extrato:
#                 print("Nenhuma transação realizada.")
#             else:
#                 for operacao, valor in extrato:
#                     print(f"{operacao}: R${valor:.2f}")
#                     print("Obrigado")
#         case _:
#             print("Opção inválida")

# __________________________________________________________

# correção do professor 

import os
import time

TEMPO = 3
TEMPO_VER_SALDO = 5

def mostrar_opcoes():
    print("1- Sacar")
    print("2- Depositar")
    print("3- Ver Saldo")
    print("4- Sair")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') # essa forma de limpar é pra funcionar em qualquer sistema operacional, como Mac, Windows, Linux etc (nome disso é ternário)

def sacar(saldo, extrato):
    while True:
        limpar_tela()
        print("------ SAQUE -----")
        try:
            valor_saque = float(input("Digite o valor que deseja sacar: "))

            if valor_saque <= 0:
                print("ERRO: O valor não pode ser menor ou igual a 0. Tente novamente.")
                time.sleep(TEMPO)
                break
            elif valor_saque > saldo:
                print("Saldo insuficiente")
                time.sleep(TEMPO)
                break
            else:
                saldo = saldo - valor_saque
                extrato.append(("Saque", valor_saque))
                print("Saque realizado com sucesso!")
                time.sleep(TEMPO)

        except ValueError:
            print("Valor inválido.")

        return saldo
    
def menu():

    extrato = []
    saldo = 1000.00

    while True:
        mostrar_opcoes()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
               saldo = sacar(saldo, extrato)
            case "2":
                pass
            case "3":
                pass
            case "4":
                print("Finalizando aplicação.")
            case _:
                print("Opção inválida.")
                time.sleep(TEMPO)

menu()