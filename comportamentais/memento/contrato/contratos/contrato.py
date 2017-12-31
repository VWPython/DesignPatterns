from contratos.estado import Estado


class Contrato(object):
    """
    Cria um contrato.
    """

    def __init__(self, data, cliente, status):
        """
        Construtor do contrato passando a data do contrato,
        o cliente do contrato e o status do contrato.
        """

        self.__data = data
        self.__cliente = cliente
        self.__status = status

    @property
    def data(self):
        """
        Pega a data do contrato.
        """

        return self.__data

    @data.setter
    def data(self, data):
        """
        Modifica a data do contrato.
        """

        self.__data = data

    @property
    def cliente(self):
        """
        Pega o cliente do contrato.
        """

        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        """
        Modifica o cliente do contrato.
        """

        self.__cliente = cliente

    @property
    def status(self):
        """
        Pega o status do contrato.
        """

        return self.__status

    @status.setter
    def status(self, status):
        """
        Modifica o status do contrato.
        """

        self.__status = status

    def executa(self):
        """
        Modifica o status do contrato de NOVO para EM ANDAMENTO,
        de EM ANDAMENTO para ACERTADO e de ACERTADO para CONCLUIDO.
        """

        if self.__status == 'NOVO':
            self.__status = 'EM ANDAMENTO'
        elif self.__status == 'EM ANDAMENTO':
            self.__status = 'ACERTADO'
        elif self.__status == 'ACERTADO':
            self.__status = 'CONCLUIDO'

    def salva_estado(self):
        """
        Salva o estado atual do contrato.
        """

        return Estado(Contrato(
            data=self.__data,
            cliente=self.__cliente,
            status=self.__status
        ))

    def restaurar_estado(self, estado):
        """
        Restaura o estado atual do contrato.
        """

        self.__cliente = estado.contrato.cliente
        self.__data = estado.contrato.data
        self.__status = estado.contrato.status
