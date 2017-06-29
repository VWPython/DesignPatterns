from abc import ABC, abstractmethod


class Carro(ABC):

    @abstractmethod
    def mostra_informacao(self):
        pass
