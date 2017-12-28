from abc import ABC, abstractmethod


class EstadoDoOrcamento(object):
    """
    Classe abstrata responsavel pelos estados do orçamento.
    """

    def __init__(self):
        """
        Constroi o estado.
        """

        self.desconto_aplicado = False

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        """
        Aplica um desconto extra no orçamento.
        """

        pass

    @abstractmethod
    def aprova(self, orcamento):
        """
        Aprova o orçamento.
        """

        pass

    @abstractmethod
    def reprova(self, orcamento):
        """
        Reprova o orçamento.
        """

        pass

    @abstractmethod
    def finaliza(self, orcamento):
        """
        Finaliza o orçamento.
        """

        pass
