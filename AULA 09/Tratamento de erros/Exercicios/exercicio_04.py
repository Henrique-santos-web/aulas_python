try:
    cores = ["Azul", "Verde", "Amarelo"]

    opcao = int(input("Escolha um numero de 0 a 2 e direi sua cor: "))

    print(f"Sua cor é: {cores[opcao]}")
except IndexError:
    print("Posição inexistente!")