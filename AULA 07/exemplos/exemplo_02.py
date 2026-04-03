gastos = {
    "luz": 200.0,
    "internet" : 100.0
}

total = 0

for valor in gastos.values():
    total += valor
    print(f"O total foi R$: {total}")