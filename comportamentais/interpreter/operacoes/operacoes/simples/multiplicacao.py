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

    def executa(self):
        """
        Retorna a multiplicação das duas expressões: esquerda e direita.
        """

        return self.__esquerda.executa() * self.__direita.executa()
