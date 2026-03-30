peso_usuario = float(input("Qual o seu peso atual? "))
altura_usuario = float(input("Qual a sua altura atual? "))

IMC = peso_usuario / (altura_usuario * altura_usuario)

IMC = round(IMC, 2)

if IMC < 18.5:
    print(f"Seu IMC: {IMC}\nSeu IMC está abaixo de 18.5 \nSinto em lhe informar, mas você está passando fome")
elif IMC >= 18.5 and IMC <= 24.9:
    print(f"Seu IMC: {IMC}\nSeu IMC está entre 18.5 e 24.9 \nParabéns, você está normal")
elif IMC >= 25.0 and IMC <= 29.9:
    print(f"Seu IMC: {IMC}\nSeu IMC está entre 25.0 e 29.9 \nCuidado, pois isto indica Excesso de peso")
else:
    print(f"Seu IMC: {IMC}\nSeu IMC está entre o 30.0 ou mais \nInfelizmente você está obeso")