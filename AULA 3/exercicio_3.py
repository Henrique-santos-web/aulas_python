ano_atual = int(input("Qual o seu ano atual? "))

# divisao_por_4 = ano_atual / 4 
# nao_dividido_por_100 = 
# divisao_por_400 = 

if (ano_atual % 4 == 0 and ano_atual % 100 != 0) or ano_atual % 400 == 0:
    print("Ano Bissesxto")
else:
    print("Ano Normal")