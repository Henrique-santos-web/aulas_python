frase = input("Digite a sua frase favorita: ").lower().strip()
palavra = frase.split()

filtro = []
for a in palavra:
    if len(a) > 4 and a[0] != 'a':
        filtro.append(a)
print(filtro)