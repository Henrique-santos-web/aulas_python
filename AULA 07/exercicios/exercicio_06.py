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


if media >= 7.0:
    print("Parabéns! Você foi aprovado")
elif media >= 5.0 and media <= 6.9:
    print("Você está em recuperação")
elif media <= 5.0:
    print("Remprovado")

maior_nota = 0
melhor_materia = ""

for materia, nota in notas.items():
    if nota > maior_nota:
        maior_nota = nota
        melhor_materia = materia
print(f"A maior nota e matéria foi: {melhor_materia} | {maior_nota} ")

# O Pyhton vai saber qual é a maior nota, pois se 8.0 for maior que 0, ele guarda o 8.0
# Neste caso como ele guardou o 8.0, ele olha todo o dicionario e não vê uma nota maior, mas se ele ver e ela for maior que 8.0
# Então ele vai guardar está nota, caso contrário, ele irá manter com a maior nota (8.0)
# IPORTANTE: Sempre atualize a variável antes de fazer a print, se não o valor dela continuará com o valor declarado (maior_nota = 0)
