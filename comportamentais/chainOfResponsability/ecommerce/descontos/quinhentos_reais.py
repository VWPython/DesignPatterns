class DescontoQuinhentosReais(object):
    """
    Desconto para compras mais de quinhentos reais.
    """

    def __init__(self, proximo_desconto):
        """
        Cria a fila de descontos a ser inserido
        """

        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        """
        Calcula o orçamento da compra com desconto.
        """

        if orcamento.valor_total > 500:
            return orcamento.valor_total * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)
