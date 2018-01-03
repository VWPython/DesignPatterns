class Item(object):
    """
    Itens que serão adicionados ao carrinho de compras.
    """

    def __init__(self, nome, valor):
        """
        Cria um item.
        """

        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        """
        Pega o valor do item.
        """

        return self.__valor

    @property
    def nome(self):
        """
        Pega o nome do item.
        """

        return self.__nome
