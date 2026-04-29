from Conta import Conta

conta = Conta("Ana")

print(conta.get_saldo())
#* Ele n acessa a conta pq o __ protege o valor (sem o get, mas apenas conta.__saldo)

print(conta.get_saldo_formatado())