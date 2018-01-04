import time


class ContaProxy(object):
    """
    Conta proxy de uso intermediario.
    """

    def __init__(self, conta):
        """
        Cria a conta intermediaria de acesso.
        """

        self.conta = conta

    def deposita(self, valor):
        """
        Deposita um valor na conta real.
        """

        print("Efetuando o depósito de R$", valor, " reais")
        time.sleep(1)
        self.conta.deposita(valor)
        print("Depósito de R$", valor, "efetuado com sucesso.")

    def saca(self, valor):
        """
        Saca um valor da conta real.
        """

        print("Efetuando o saque de R$", valor, " reais")
        time.sleep(1)
        self.conta.saca(valor)
        print("Saque de R$", valor, "efetuado com sucesso.")

    @property
    def saldo(self):
        """
        Pega o saldo.
        """

        print("Verificando saldo...")
        return self.conta.saldo
