from abc import ABC, abstractmethod


class Emissor(ABC):

    @abstractmethod
    def envia(self, mensagem):
        pass
