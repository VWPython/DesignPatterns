from abc import ABC, abstractmethod


class Boleto(ABC):
    """
    Classe abstrata que serve de template para gerar boletos.
    """

    @abstractmethod
    def sacado(self):
        """
        Pessoa ou empresa resposável pelo pagamento do boleto
        """

        pass

    @abstractmethod
    def cedente(self):
        """
        Pessoa ou empresa que receberá o pagamento do boleto
        """

        pass

    @abstractmethod
    def valor(self):
        """
        Valor do boleto.
        """

        pass

    @abstractmethod
    def vencimento(self):
        """
        Vencimento do boleto.
        """

        pass

    @abstractmethod
    def numero(self):
        """
        Número do boleto.
        """

        pass

    @abstractmethod
    def imprime(self):
        """
        Imprime o boleto.
        """

        pass
