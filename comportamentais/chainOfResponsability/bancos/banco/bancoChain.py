from abc import ABC, abstractmethod


class BancoChain(ABC):

    def __init__(self, banco_id):
        """
        Cria uma fila de bancos para efetuar pagamento
        """

        self.proximo = None
        self.banco_id = banco_id

    def insere(self, banco):
        """
        Modifica para o próximo banco caso não este tenha sido passado.
        """

        if (self.proximo is None):
            self.proximo = banco
        else:
            self.proximo.insere(banco)

    def efetua_pagamento(self, banco_id):
        """
        Efetua o pagamento se o banco estiver cadastrado
        caso contrario passe para o próximo banco.
        """

        if (self.__pode_efetuar_pagamento(banco_id)):
            self.pagar()
        else:
            if (self.proximo is None):
                raise NameError("Exceção: Banco não cadastrado")

            self.proximo.efetua_pagamento(banco_id)

    def __pode_efetuar_pagamento(self, banco_id):
        """
        Verifica se o banco foi cadastrado
        """

        if (self.banco_id == banco_id):
            return True
        else:
            return False

    @abstractmethod
    def pagar(self):
        """
        Metódo que deve ser implementado pelos bancos.
        """

        pass
