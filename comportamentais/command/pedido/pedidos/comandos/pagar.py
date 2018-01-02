from pedidos.comando import Comando


class Pagar(Comando):
    """
    Paga o pedido.
    """

    def __init__(self, pedido):
        """
        Cria o comando pagar e insere o pedido na qual o comando irá agir.
        """

        self.__pedido = pedido

    def executa(self):
        """
        Executa o comando para pagar o pedido.
        """

        self.__pedido.paga()
