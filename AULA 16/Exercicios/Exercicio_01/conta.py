class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0.0


    def get_saldo(self):
        return self.__saldo