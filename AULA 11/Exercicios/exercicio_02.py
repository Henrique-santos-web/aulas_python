lista_vip = ["Marcos", "Henrique", "Arthur"]

nome_na_lista = input("Olá, qual o seu nome? ").title()

if nome_na_lista in lista_vip:
    print(f"Pode entrar senhor {nome_na_lista}")
else:
    print("Esta é uma festa privada e o seu nome não está. Por favor se retire")

