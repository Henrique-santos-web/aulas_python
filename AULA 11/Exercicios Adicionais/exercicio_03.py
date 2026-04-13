extrato = []

saldo = float(1000.00)


while True:

    opcao = (input("Escolha uma das opções abaixo: \n1- Sacar\n2- Depositar\n3- Ver Saldo\n4- Sair\n"))

    match opcao:
        case "1":
            saque = float(input("Quanto o senhor deseja sacar? "))
            if saque > saldo :
                print("Saldo insuficiente!")
            elif saque <= saldo:
                saldo -= saque
                extrato.append("Saque", saldo)
                print(f"Saque no valor de R${saque} realizado com sucesso.\nSeu saldo atual é de: R${saldo}")
            else:
                print("ERRO")
        case "2":
            depositar = float(input("Quanto deseja depositar? "))
            if depositar > 0:
                saldo += depositar
                extrato.append(("Deposito", depositar))
                print("Depósito realizado com sucesso!")
            else:
                print("Erro! Digite um valor positivo...")
        case "3":
            print(f"Seu saldo é de: R${saldo:.2f}")
        case "4":
            if not extrato:
                print("Nenhuma transação realizada.")
            else:
                for operacao, valor in extrato:
                    print(f"{operacao}: R${valor:.2f}")
                    print("Obrigado")
        case _:
            print("Opção inválida")