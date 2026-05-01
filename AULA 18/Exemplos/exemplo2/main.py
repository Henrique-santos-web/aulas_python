from PagamentoCartao import PagamentoCartao
from PagamentoPix import PagamentoPix
from PagamentoPaypal import PagamentoPaypal


def realizar_checkout(metodo, valor):
    metodo.processar(valor)
    print("Obrigado por comprar!")



cartao = PagamentoCartao()
pix = PagamentoPix()
paypal = PagamentoPaypal()

realizar_checkout(cartao, 100.00)
realizar_checkout(pix, 50.00)
realizar_checkout(paypal, 10.00)