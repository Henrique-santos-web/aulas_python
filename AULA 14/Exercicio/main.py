import catalogo


def mostrar_menu():
    catalogo.limpar_console()
    print("\n" + "=" * 48)
    print("                  CineLog")
    print("="*40)
    print("1. Adicionar Filme/Serie")
    print("2. Ver o meu catalogo")
    print("3. Pesquisar por titulo")
    print("4. Pesquisar por genero")
    print("5. Pesquisar por ano")
    print("6. Sair")
    print("")
    print("")
    print("="*48)


def iniciar_app()
    meus_filmes = catalogo.carregar_dados()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1"
                catalogo.adicionar_filmes(meus_filmes)

            case "2"
                catalogo.listar_filmes(meus_filmes)
            case "3"
                catalogo.pesquisar_por_filme(meus_filmes)
            case "4"
                catalogo.pesquisar_por_genero(meus_filmes)
            case "5"
                catalogo.pesquisar_por_ano(meus_filmes)
            case "6"
                catalogo.limpar_console()
                catalogo.salvar_dados(meus_filmes)

            case ""

            #treminar em casa olhando o código do professor e tentando entender o que está acontecendo 