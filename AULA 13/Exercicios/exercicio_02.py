numero = int(input("Digite um numero inteiro positivo: "))

resultado = 0

for par in range(0, numero + 1, 2):
    resultado += par
print(f"A soma dos pares é: {resultado}")