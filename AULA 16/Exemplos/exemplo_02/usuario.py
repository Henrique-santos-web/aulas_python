class Usuario:
    def __init__(self):
        self.__senha = "123"

    def se_senha(self, nova_senha):
        if len(nova_senha) >= 5:
            self.__senha = nova_senha
            print("Senha atualizada")
        else:
            print("Senha ERRO")