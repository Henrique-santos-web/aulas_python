from conta import Conta

if __name__ == "__main__":
    meu_usuario = Conta("João")

#* eu tenho que criar uma variavel que vai guardar a classe
#* E acessar nessa classe a conta_usuario
    print(f"Olá, {meu_usuario.titular}. O seu saldo é de: {meu_usuario.get_saldo()}")