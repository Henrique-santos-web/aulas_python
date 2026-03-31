conta = float(input("Olá, qual o valor da conta? "))

troco = print(f"Certo! O valor da conta é de: R${conta}.\n")

gorjeta = conta * 0.10

print(f"Caso o senhor  queira dar uma gorjeta de 10%, ficaria no valor de: R${gorjeta}")
total = conta + gorjeta
print(f"\nO valor total da conta com a gorjeta é de: {total}")