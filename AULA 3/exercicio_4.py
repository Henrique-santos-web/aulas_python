saldo = float(1000)

opcao = int(input("Escolha uma das opções abaixo: \n1- Saldo\n2- Sacar\n3- Sair\n"))

if opcao == 1:
    print(f"Seu saldo é de: R${saldo}")
elif opcao == 2:
    saque = float(input("Quanto o senhor deseja sacar? "))
    if saque > saldo :
        print("Saldo insuficiente!")
    elif saque <= saldo:
        saldo_atual = saldo - saque
        print(f"Saque no valor de R${saque} realizado com sucesso.\nSeu saldo atual é de: R${saldo_atual}")
    else:
        print("ERRO")
elif opcao == 3:
    print("Obrigado!")
else:
    print("ERRO")