class Subtracao(object):
    """
    Operação simples de subtração
    """

    def __init__(self, esquerda, direita):
        """
        Constroi a operação simples de subtração passando a expressão do lado
        esquerdo e a expressão do lado direito.
        """

        self.__esquerda = esquerda
        self.__direita = direita

    def executa(self):
        """
        Retorna a subtração das duas expressões: esquerda e direita.
        """
        return self.__esquerda.executa() - self.__direita.executa()
