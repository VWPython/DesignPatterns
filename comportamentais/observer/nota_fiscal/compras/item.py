class Item(object):
    """
    Item da compra.
    """

    def __init__(self, descricao, valor):
        """
        Cria o item da compra.
        """

        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        """
        Descrição do item.
        """

        return self.__descricao

    @property
    def valor(self):
        """
        Valor do item.
        """

        return self.__valor
