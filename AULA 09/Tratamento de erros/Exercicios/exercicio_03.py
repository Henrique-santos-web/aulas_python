while True:
    try:
        nascimento = int(input("Qual ano você nasceu? "))
        resultado = 2026 - nascimento
        print(f"Você tem {resultado} anos!")
        break
    except ValueError:
        print("Apenas números são permitidos")