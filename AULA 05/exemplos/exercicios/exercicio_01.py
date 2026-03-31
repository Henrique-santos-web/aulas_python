soma = 0

while True:
    numero = int(input("Digite um numero: "))

    if numero == 0:
        break
    soma += numero
   
print(f"A soma: {soma}")