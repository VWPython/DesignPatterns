class Estado(object):

    def __init__(self, contrato):
        """
        Construtor do estado do contrato.
        """

        self.__contrato = contrato

    @property
    def contrato(self):
        """
        Pega o contrato atual
        """

        return self.__contrato
