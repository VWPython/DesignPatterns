class Multiplicacao(object):
    """
    Operação simples de multiplicação.
    """

    def __init__(self, esquerda, direita):
        """
        Constroi a operação simples de multiplicação passando a
        expressão do lado esquerdo e a expressão do lado direito.
        """

        self.__esquerda = esquerda
        self.__direita = direita

    @property
    def expressao_esquerda(self):
        """
        Pega a expressão esquerda.
        """

        return self.__esquerda

    @property
    def expressao_direita(self):
        """
        Pega a expressão direita.
        """

        return self.__direita

    def executa(self):
        """
        Retorna a multiplicação das duas expressões: esquerda e direita.
        """

        return self.__esquerda.executa() * self.__direita.executa()

    def aceita(self, visitante):
        """
        Aceita a impressão de multiplicação.
        """

        return visitante.visita_multiplicacao(self)
