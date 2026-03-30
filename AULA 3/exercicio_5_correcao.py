import random

pc = random.choice(["Pedra", "Papel", "Tesoura"])

jogador = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()

print(f"Escolha do pc: {pc}")
print(f"Escolha do jogador: {jogador}")

if jogador == pc:
    print("Empate")
elif (jogador == "Pedra" and pc == "Tesoura") or (jogador == "Pedra" and pc == "Papel") or (jogador == "Tesoura" and pc == "Papel"):
    print("Você ganhou!")
elif jogador not in ["Pedra", "Papel", "Tesoura"]:
    print("Jogada inválida. Você sabe escrever? Barbaridade")
else:
    print("Você perdeu")

    # correção do professor