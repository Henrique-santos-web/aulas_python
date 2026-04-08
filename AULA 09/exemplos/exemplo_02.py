def analisar_numeros(n1, n2):
    soma = n1 + n2
    dif = n1 - n2
    return soma, dif

res_soma, res_dif = analisar_numeros(20, 5)

print(f"Soma: {res_soma} | Sub: {res_dif}")