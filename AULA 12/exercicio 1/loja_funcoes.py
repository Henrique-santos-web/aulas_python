def calcular_desconto(preco):
    return preco - (preco * 0.15)

if __name__ == "__main__":
    print("Testando a função")
    print(calcular_desconto(100))
