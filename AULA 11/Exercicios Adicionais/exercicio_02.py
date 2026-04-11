def cadastrar_usuario():

    while True:
        try:
            idade_usuario = int(input("Qual a sua idade? "))

            if idade_usuario < 0 or idade_usuario > 120:
                print("Idade inválida")
                continue
            else:
                while True:
                    try:
                        nome_usuario = input("Qual o seu nome? ")
                        break
                    except:
                        print("Digite apenas letras")
                        continue

        except ValueError:
            print("Digite apenas números!")

            return nome_usuario, idade_usuario



cracha = {
    "nome": nome_usuario,
    "idade": idade_usuario
}
cadastrar_usuario()
