from loja.pagamentoCommand import PagamentoCommand


class Boleto(PagamentoCommand):
    """
    Pagamento com boleto bancario.
    """

    def processa_compra(self, compra):
        """
        Processa a compra com boleto bancario como forma de pagamento
        """

        print("Boleto criado!\n" + compra.nota_fiscal)
