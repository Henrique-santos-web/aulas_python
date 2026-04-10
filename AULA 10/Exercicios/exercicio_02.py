numero = 1

# * Não executa do 1 ao 5, pois se o número for MENOR (4, 3, 2, 1, -1...) ou IGUAL ao 5 (5 por si só é igual a ele mesmo), ele vai adicionar +1.
# * 6 é MAIOR e não é IGUAL ao 5, por isso é mostrado.
while numero <= 5:
    numero = numero + 1
print(f"Número: {numero}")