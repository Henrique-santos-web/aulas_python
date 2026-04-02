produtos = {
    "Chocolate": 7.99,
    "Notebook": 3500.00,
    "Mouse": 150.00
}
print('Temos esses produtos: \n- Chocolate\n- Notebook\n- Mouse\n')
produto_desejado = input("Qual o produto que você quer? \n")

if produto_desejado == "Chocolate":
    print(produtos["Chocolate"])
elif produto_desejado == "Notebook":
    print(produtos["Notebook"])
elif produto_desejado == "Mouse":
    print(produtos["Mouse"])
else:
    print("Digite um produto da lista")
