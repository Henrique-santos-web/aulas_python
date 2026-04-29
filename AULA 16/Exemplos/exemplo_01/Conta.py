class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0.0

    def get_saldo(self):
        return self.__saldo
    
    
    def get_saldo_formatado(self):
        return f"R$ {self.__saldo:.2f}"