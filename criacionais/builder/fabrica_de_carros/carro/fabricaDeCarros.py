from abc import ABC, abstractmethod
from carro.produto import Carro


class FabricaDeCarros(ABC):

    def __init__(self):
        self.carro = Carro()

    @abstractmethod
    def define_preco(self, preco):
        pass

    @abstractmethod
    def define_motor(self, motor):
        pass

    @abstractmethod
    def define_ano_de_fabricacao(self, ano_de_fabricacao):
        pass

    @abstractmethod
    def define_modelo(self, modelo):
        pass

    @abstractmethod
    def define_montadora(self):
        pass

    def constroi_carro(self):
        return self.carro

