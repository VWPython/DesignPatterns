from abc import ABC, abstractmethod


class PrototipoDeCarro(ABC):

    def __init__(self):
        self.__valor_da_compra = 0.0

    @abstractmethod
    def exibe_informacao(self):
        pass

    @abstractmethod
    def clonar(self):
        pass

    @property
    def valor_da_compra(self):
        return self.__valor_da_compra

    @valor_da_compra.setter
    def valor_da_compra(self, valor_da_compra):
        self.__valor_da_compra = valor_da_compra
