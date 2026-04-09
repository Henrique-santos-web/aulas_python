# def converter_dolar():
#     valor_dolar = 1
#     taxa_cambio = 5.10
#     real = valor_dolar * taxa_cambio
#     return real
# converter_dolar()

# conversao = converter_dolar()
# print(conversao)



# correção professor

def converter_dolar(valor_dolar, taxa_cambio):
    valor_convertido = valor_dolar * taxa_cambio
    return valor_convertido

valor_final = converter_dolar(100, 5.10)

print(f"O valor convertido fica em: R${valor_final:.2f}")