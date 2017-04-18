from abc import ABCMeta, abstractmethod
from carro.produto import Carro

class FabricaDeCarros(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.carro = Carro()

    @abstractmethod
    def define_preco(self):
        pass

    @abstractmethod
    def define_motor(self):
        pass

    @abstractmethod
    def define_ano_de_fabricacao(self):
        pass

    @abstractmethod
    def define_modelo(self):
        pass

    @abstractmethod
    def define_montadora(self):
        pass

    def constroi_carro(self):
        return self.carro

