# numero_digitado = int(input("Digite um numero que você queira ver a tabuada: "))

# for numero_digitado in range(0, 11, 1*numero_digitado):
#     print(f"A tabuada do numero {numero_digitado} é: {numero_digitado}")

# correção do professor abaixo

num_tabuada = int(input("Digite um numero para inicar a tabuada: "))
print(f"==== Tabuada do numero {num_tabuada} ====")
for multiplicador in range(1, 11):
    print(f"{num_tabuada} X {multiplicador} = {num_tabuada * multiplicador}")

print("Fim da tabuada")