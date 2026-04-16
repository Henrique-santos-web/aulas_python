import json

filme = {
    "nome":"Sexta_feira 13",
    "ano":"1980"
}

with open("AULA 12\\exercicio 1\\filme.json", "w") as arquivo:
    json.dump(filme, arquivo)

with open("AULA 12\\exercicio 1\\filme.json", "r") as arquivo:
   filme_recuperado = json.load(arquivo)

print(filme["ano"])