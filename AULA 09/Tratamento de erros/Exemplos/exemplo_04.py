while True:
    try:
        idade = int(input("Idade : "))

        if idade <= 0:
            raise ValueError()
        break
    except ValueError:
        print("Apenas números são válidos...")
print(f"Idade registrada: {idade}")