class Dados(object):
    """
    Classe responsavel pelos dados da tabela.
    """

    def __init__(self, a, b, c):
        """
        Constroi os dados.
        """

        self.__valorA = a
        self.__valorB = b
        self.__valorC = c

    @property
    def valorA(self):
        """
        Pega o valor A
        """

        return self.__valorA

    @property
    def valorB(self):
        """
        Pega o valor B
        """

        return self.__valorB

    @property
    def valorC(self):
        """
        Pega o valor C
        """

        return self.__valorC
