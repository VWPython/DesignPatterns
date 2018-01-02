class No(object):
    """
    Classe responsavel pelos nós da arvore binária de busca.
    """

    def __init__(self, chave):
        """
        Cria um nó da arvore.
        """

        self.__chave = chave
        self.__esquerda = None
        self.__direita = None

    def __str__(self):
        """
        Retorna o nó em forma de string.
        """

        return str(self.__chave)

    @property
    def chave(self):
        """
        Pega a chave do nó.
        """

        return self.__chave

    @property
    def esquerda(self):
        """
        Pega o nó a esquerda do nó chave.
        """

        return self.__esquerda

    @esquerda.setter
    def esquerda(self, no_esquerdo):
        """
        Modifica o nó esquerdo do nó chave.
        """

        self.__esquerda = no_esquerdo

    @property
    def direita(self):
        """
        Pega o nó a direita do nó chave.
        """

        return self.__direita

    @direita.setter
    def direita(self, no_direito):
        """
        Modifica o nó direito do nó chave.
        """

        self.__direita = no_direito
