from abc import ABC, abstractmethod


class Compartilha(ABC):

    @abstractmethod
    def adquire(self, numero):
        pass

    @abstractmethod
    def libera(self, numero):
        pass
