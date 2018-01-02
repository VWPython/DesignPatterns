class Numero(object):
    """
    Classe que cria os números.
    """

    def __init__(self, numero):
        """
        Constroi o número.
        """

        self.__numero = numero

    def executa(self):
        """
        Retorna o número.
        """

        return self.__numero

    def aceita(self, visitante):
        """
        Aceita a impressão do número.
        """

        return visitante.visita_numero(self)
