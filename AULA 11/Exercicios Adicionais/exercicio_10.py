# correção do professor e estudar essa correção no final de semana

def calcular_salario(valor_base, hora_extra = 0, bonificacao = False):
    salario = valor_base

    valor_das_horas = hora_extra * 50.00
    salario += valor_das_horas

    if bonificacao == True:
        salario += salario * 0.15

    return f"R$ {salario:.2f}"

print("--- CALCULADORA SALARIO ---")

salario1 = calcular_salario(3000.00)
print(f"Cenário 1 (Apenas Base): {salario1}")

salario2 = calcular_salario(3000.00, 10)
print(f"Cenário 2 (Salaio + 10h Extras): {salario2}")

salario3 = calcular_salario(3000.00, 10, True)
print(f"Cenário 3 (Salario + 10h + Bonificação): {salario3}")

salario4 = calcular_salario(3000.00, bonificacao = True)
print(f"Cenário 4 (Salario + Bonificação): {salario4}")