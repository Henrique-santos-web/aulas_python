# notas = {
#     "Matemática":8.0,
#     "História": 7.5
# }

# soma = 0

# for nota in notas:
# desafio não concluído

# ---------------------

# Desafio concluído e eplicado por uma IA

# 1. Criando o dicionário de notas
notas = {
    "Matemática": 8.0, 
    "História": 7.5
}

# 2. Inicializando a variável de soma
soma = 0

# 3. Iterando pelos valores e calculando a média
for nota in notas.values():
    soma += nota

media = soma / len(notas)

print(f"A média da turma é: {media}")


