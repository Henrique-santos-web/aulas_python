from loja_funcoes import calcular_desconto

valor_compra = float(input("Digite o valor da compra: "))

print(f"O valor final da comprea com desconto é: R$ {calcular_desconto(valor_compra)}")