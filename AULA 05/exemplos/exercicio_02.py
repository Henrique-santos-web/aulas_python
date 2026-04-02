# numero = int(input("Digite um numero: "))

# for i in range(1, 11):
#     if numero / 2 == 0:
#         continue
#     elif numero != 0:
#         i = numero
#         print(f"este numero é impar: {i}")
#     else:
#         print("Digite um numero interiro!!")

#correção do professor logo abaixo

for numero in range(1, 11):

    if numero % 2 == 0:
        continue
    print(f"{numero}")