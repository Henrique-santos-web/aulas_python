while True:
    opcao = input("[1] Pizza, [2] Hambúrguer, [0] Sair: ")
    match opcao:
        case "1":
            print("Sua Pizza está sendo preparada")
        case "2":
            print("Seu Hambúrguer está sendo preparado")
        case "0":
            print("Finalizando...")
            break
        case _:
            print("Opção inválida")