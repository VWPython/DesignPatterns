from pedidos.comando import Comando


class Concluir(Comando):
    """
    Conclui o pedido.
    """

    def __init__(self, pedido):
        """
        Cria o comando concluir e insere o pedido na qual o comando irá agir.
        """

        self.__pedido = pedido

    def executa(self):
        """
        Executa o comando para concluir o pedido.
        """

        self.__pedido.finaliza()
