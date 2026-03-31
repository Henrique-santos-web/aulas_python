secreto = 7
palpite = 0

while palpite != secreto:
    palpite = int(input("Digite o seu palpite: "))

    if palpite != secreto:
        print("Errado! Tente novamente.")

print("Parabéns! Você acertou o número secreto.")