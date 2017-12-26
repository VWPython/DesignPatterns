from abc import ABC, abstractmethod

class PagamentoCommand(ABC):

    @abstractmethod
    def processa_compra(self, compra):
        pass
