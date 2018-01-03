class DescontoCincoItens(object):
    """
    Desconto por cinco itens no carrinho.
    """

    def __init__(self, proximo_desconto):
        """
        Cria a fila de descontos a ser inserido
        """

        self.__proximo_desconto = proximo_desconto

    def calcula(self, carrinho):
        """
        Calcula o orçamento da compra com desconto.
        """

        if carrinho.total_de_itens >= 5:
            return carrinho.valor_total * 0.1
        else:
            return self.__proximo_desconto.calcula(carrinho)
