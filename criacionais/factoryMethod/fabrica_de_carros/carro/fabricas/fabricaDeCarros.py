from abc import ABC, abstractmethod


class FabricaDeCarros(ABC):

    @abstractmethod
    def constroi_carro(self):
        pass
