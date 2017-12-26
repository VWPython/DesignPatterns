from abc import ABC, abstractmethod

class Colleague(ABC):

    def __init__(self, mediator):
        self.mediator = mediator

    def envia_mensagem(self, mensagem):
        self.mediator.envia(mensagem, self)

    @abstractmethod
    def recebe_mensagem(self, mensagem):
        pass
