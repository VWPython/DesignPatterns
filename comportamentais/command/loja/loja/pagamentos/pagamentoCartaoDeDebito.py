from loja.pagamentoCommand import PagamentoCommand


class CartaoDeDebito(PagamentoCommand):
    """
    Pagamento utilizando cartão de debito.
    """

    def processa_compra(self, compra):
        """
        Processa a compra utilizando cartão de debito como forma de
        pagamento.
        """

        print("Cartão de debito aceito!\n" + compra.nota_fiscal)
