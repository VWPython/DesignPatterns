from abc import ABC, abstractmethod


class PagamentoCommand(ABC):
    """
    Classe abstrata que cria as formas de pagamento.
    """

    @abstractmethod
    def processa_compra(self, compra):
        """
        Processa a compra
        """

        pass
