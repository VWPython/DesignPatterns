from abc import ABC, abstractmethod

class DadosObserver(ABC):

    def __init__(self, dados):
        self.dados = dados

    @abstractmethod
    def atualiza(self):
        pass
