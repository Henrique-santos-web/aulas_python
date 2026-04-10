opcao = input("1- Ver, 2- Editar, 3- Sair: ")

match opcao:
    case "1":
        print("Vendo arquivo...")
    case "2":
        print("Editando Arquivo...")
    case "3":
        print("Saindo...")
    case _:
        print("Opção inválida.")