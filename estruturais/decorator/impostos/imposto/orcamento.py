class Orcamento(object):
    """
    Cria o orçamento que será aplicado os impostos.
    """

    def __init__(self, valor):
        """
        Constroi o orçamento.
        """

        self.__valor = valor

    @property
    def valor(self):
        """
        Valor do orçamento.
        """

        return self.__valor
