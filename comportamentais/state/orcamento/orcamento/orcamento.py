from orcamento.estados.em_aprovacao import EmAprovacao


class Orcamento(object):
    """
    Classe responsavel pelo orçamento.
    """

    def __init__(self):
        """
        Cria o orçamento.
        """

        self.__itens = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    @property
    def total(self):
        """
        Calculo do orçamento total.
        """

        total = 0.0

        for item in self.__itens:
            total += item.valor

        return total - self.__desconto_extra

    def adiciona_item(self, item):
        """
        Adiciona um item ao orçamento total.
        """

        self.__itens.append(item)

    def aprova(self):
        """
        Aprova orçamento.
        """

        self.estado_atual.aprova(self)

    def reprova(self):
        """
        Reprova o orçamento.
        """

        self.estado_atual.reprova(self)

    def finaliza(self):
        """
        Finaliza o orçamento.
        """

        self.estado_atual.finaliza(self)

    def aplica_desconto_extra(self):
        """
        Aplica desconto extra no orçamento.
        """

        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        """
        Adiciona um desconto extra ao orçamento.
        """

        self.__desconto_extra += desconto
