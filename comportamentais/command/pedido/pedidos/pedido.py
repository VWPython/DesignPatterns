from datetime import date


class Pedido(object):
    """
    Classe responsavel pelos pedidos.
    """

    def __init__(self, cliente, valor):
        """
        Cria um pedido.
        """

        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        """
        Paga o pedido.
        """

        self.__status = 'PAGO'
        print("O pedido do cliente", self.cliente, "foi pago.")

    def finaliza(self):
        """
        Finaliza o pedido.
        """

        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'
        print("O pedido do cliente", self.cliente ,"foi entregue na data", self.data_finalizacao)

    @property
    def cliente(self):
        """
        Pega o cliente do pedido.
        """

        return self.__cliente

    @property
    def valor(self):
        """
        Pega o valor do pedido.
        """

        return self.__valor

    @property
    def status(self):
        """
        Pega o status do pedido.
        """

        return self.__status

    @property
    def data_finalizacao(self):
        """
        Pega a data de finalização do pedido.
        """

        return self.__data_finalizacao
