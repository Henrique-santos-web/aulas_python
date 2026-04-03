cliente = {
    "nome" : "Ana",
    "plano":"Premium"
}

print(cliente.items())

for chave, valor in cliente.items():
    print(f"{chave} = {valor}")