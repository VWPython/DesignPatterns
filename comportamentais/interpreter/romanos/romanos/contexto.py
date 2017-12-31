class Contexto(object):
    """
    Número romano.
    """

    def __init__(self, numero=''):
        """
        Controi o número romano.
        """

        self.__numero_romano = numero
        self.__resultado = 0

    @property
    def numero_romano(self):
        """
        Retorna o número romano
        """

        return self.__numero_romano

    @numero_romano.setter
    def numero_romano(self, numero):
        """
        Modifica o número romano.
        """

        self.__numero_romano = numero

    @property
    def resultado(self):
        """
        Retorna o resultado em decimal ou romano
        """

        return self.__resultado

    @resultado.setter
    def resultado(self, resultado):
        """
        Modifica o resultado em romano
        """

        self.__resultado = resultado
