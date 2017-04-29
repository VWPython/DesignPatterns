from loja.loja import Loja
from loja.pagamentos.pagamentoCartaoDeCredito import PagamentoCartaoDeCredito
from loja.pagamentos.pagamentoCartaoDeDebito import PagamentoCartaoDeDebito
from loja.pagamentos.pagamentoBoleto import PagamentoBoleto

def main():

    lojas_americanas = Loja("Lojas Americanas")
    lojas_americanas.executa_compra(999.00, PagamentoCartaoDeCredito())
    lojas_americanas.executa_compra(49.90, PagamentoBoleto())
    lojas_americanas.executa_compra(99.00, PagamentoCartaoDeDebito())

    casas_bahia = Loja("Casas Bahia")
    casas_bahia.executa_compra(19.00, PagamentoCartaoDeCredito())

if __name__ == '__main__':
    main()
