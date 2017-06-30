from abc import ABC, abstractmethod


class FabricaDeCarros(ABC):

    @abstractmethod
    def constroi_carro_sedan(self, modelo):
        pass

    @abstractmethod
    def constroi_carro_popular(self, modelo):
        pass
