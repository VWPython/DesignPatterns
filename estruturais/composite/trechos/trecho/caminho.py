from trecho.trecho import Trecho


class Caminho(Trecho):
    """
    Caminho com um conjunto de trechos.
    """

    def __init__(self):
        """
        Constroi o caminho.
        """

        self.caminho = []

    def adiciona(self, trecho):
        """
        Adiciona trechos ao caminho.
        """

        self.caminho.append(trecho)

    def remove(self, trecho):
        """
        Remove um trecho do caminho.
        """

        self.caminho.remove(trecho)

    def imprime(self):
        """
        Imprime o caminho.
        """

        for trecho in self.caminho:
            trecho.imprime()
