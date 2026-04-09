try:
    preco = int(input("Qual o valor do produto? "))
    print(preco)

except ValueError:
    print("Apenas numeros são válidos")