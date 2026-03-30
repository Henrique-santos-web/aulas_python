import random
pc = random.choice(["Pedra", "Papel", "Tesoura"])

pedra = int(print("1- Pedra"))
papel = int(print("2- Papel"))
tesoura = int(print("3- Tesoura"))
opcao = int(input("Qual opção você escolhe? "))


if opcao == pc:
    print("Deu empate")
elif opcao == 1 and pc ("Tesoura"):
    print("Você Ganhou!")
elif opcao == 2 and pc ("Pedra"):
    print("Você ganhou")
elif opcao == 3 and pc ("Papel"):
    print("Você ganhou")
else:
    print("Você perdeu")

    # Não consegui, então vamos para a correção do professor