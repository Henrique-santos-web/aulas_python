palavra = input("Digite uma palavra: ")

print(f"A palavra {palavra} vira: ")
for letra in palavra:
    print(f"-{letra}", end=" ")