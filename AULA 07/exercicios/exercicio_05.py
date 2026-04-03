cardapio = {
    "Pizza": 40.00,
    "Cachorro_Quente": 20.00,
    "Pastel":10.00,
    "Suco":12.00
}

for lanche, valor in cardapio.items(): 
    print(f"Comida: {lanche} | R$: {valor}")