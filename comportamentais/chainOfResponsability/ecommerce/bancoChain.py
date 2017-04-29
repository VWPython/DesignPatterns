from abc import ABC, abstractmethod

class BancoChain(ABC):

    def __init__(self, banco_id):
        self.next = None
        self.banco_id = banco_id

    def modifica_proximo(self, banco):
        if (self.next == None):
            self.next = banco
        else:
            self.next.modifica_proximo(banco)

    def efetua_pagamento(self, banco_id):
        if (self.__pode_efetuar_pagamento(banco_id)):
            self.pagar()
        else:
            if (self.next == None):
                raise NameError("Exceção: Banco não cadastrado")
            self.next.efetua_pagamento(banco_id)

    def __pode_efetuar_pagamento(self, banco_id):
        if (self.banco_id == banco_id):
            return True
        else:
            return False

    @abstractmethod
    def pagar(self):
        pass
