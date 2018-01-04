class Conta(object):
    """
    Conta padrão de uso.
    """

    def __init__(self, saldo=0.0):
        """
        Cria a conta padrão.
        """

        self.__saldo = saldo

    def deposita(self, valor):
        """
        Deposita um valor na conta.
        """

        self.__saldo += valor

    def saca(self, valor):
        """
        Saca um valor da conta.
        """

        self.__saldo -= valor

    @property
    def saldo(self):
        """
        Pega o saldo.
        """

        return self.__saldo
