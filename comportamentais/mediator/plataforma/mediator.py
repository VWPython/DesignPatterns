from abc import ABC, abstractmethod

class Mediator(ABC):

    @abstractmethod
    def envia(mensagem, colleague):
        pass
