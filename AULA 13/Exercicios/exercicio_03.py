def contar_vogais(texto):
    texto = texto.lower()
    total = 0
    for letra in texto:
        if letra in "aeiou":
            total += 1
    return total  # A função devolve apenas o NÚMERO


# 1. Primeiro pegamos o texto do usuário
palavra = input("Digite uma palavra: ")

# 2. Chamamos a função passando esse texto e guardamos o retorno
quantidade = contar_vogais(palavra)

# 3. Exibimos o resultado usando as variáveis que temos aqui fora
print(f"A palavra '{palavra}' tem {quantidade} vogais.")