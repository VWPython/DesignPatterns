from abc import ABC, abstractmethod


class CarroPopular(ABC):

    @abstractmethod
    def mostra_informacao(self):
        pass
