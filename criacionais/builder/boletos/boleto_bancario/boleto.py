from abc import ABC, abstractmethod


class Boleto(ABC):

    @abstractmethod
    def sacado(self):
        # Pessoa ou empresa resposável pelo pagamento do boleto
        pass

    @abstractmethod
    def cedente(self):
        # Pessoa ou empresa que receberá o pagamento do boleto
        pass

    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def vencimento(self):
        pass

    @abstractmethod
    def numero(self):
        pass

    @abstractmethod
    def imprime(self):
        pass
