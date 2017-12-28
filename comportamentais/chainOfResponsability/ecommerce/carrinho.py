class Carrinho(object):
    """
    Classe que armazena os itens e calcula o orçamento.
    """

    def __init__(self):
        """
        Cria a lista de itens do carrinho de compras para
        calcular o orçamento.
        """

        self.__itens = []

    @property
    def valor_total(self):
        """
        Valor total do orçamento de acordo com os itens.
        """

        total = 0.0

        for item in self.__itens:
            total += item.valor

        return total

    @property
    def total_de_itens(self):
        """
        Pega o total de itens.
        """

        return len(self.__itens)

    def adiciona_item(self, item):
        """
        Adiciona itens ao carrinho.
        """

        self.__itens.append(item)
