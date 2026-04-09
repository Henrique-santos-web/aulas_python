def calculadora_dobro_e_triplo(num):
    dobro = num * 2
    triplo = num * 3
    return dobro, triplo


numero = int(input("Digite um valor: "))

valor_dobro, valor_triplo = calculadora_dobro_e_triplo(numero)

print(f"O dobro de {numero} é {valor_dobro} e o triplo é {valor_triplo}")