class Soma(object):
    """
    Operação simples de soma.
    """

    def __init__(self, esquerda, direita):
        """
        Constroi a operação simples de soma passando a expressão do lado
        esquerdo e a expressão do lado direito.
        """

        self.__esquerda = esquerda
        self.__direita = direita

    def executa(self):
        """
        Retorna a soma das duas expressões: esquerda e direita.
        """

        return self.__esquerda.executa() + self.__direita.executa()
