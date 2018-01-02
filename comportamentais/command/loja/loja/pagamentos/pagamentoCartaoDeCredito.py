from loja.pagamentoCommand import PagamentoCommand


class CartaoDeCredito(PagamentoCommand):
    """
    Pagamento com cartão de crédito.
    """

    def processa_compra(self, compra):
        """
        Processa a compra utilizando cartão de crédito como forma de
        pagemento.
        """

        print("Cartão de credito aceito!\n" + compra.nota_fiscal)
