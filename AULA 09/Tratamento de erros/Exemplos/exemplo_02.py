try:
    num1 = int(input("Número: "))
    num2 = int(input("Dividir por: "))
    res = num1 / num2
    print(f"Resultado: {res}")

except ValueError:
    print("ERRO: Não é um número válido!")
except ZeroDivisionError:
    print("ERRO: Não pode dividir por zero!")