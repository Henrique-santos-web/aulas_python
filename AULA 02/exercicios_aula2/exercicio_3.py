idade = int(input("Qual a sua idade? "))

if idade < 13:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Você está internado ou em um lugar melhor (se é que me entende 💀)")