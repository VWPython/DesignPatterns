from abc import ABCMeta, abstractmethod

class PrototipoDeCarro(object):

    __metaclass__ = ABCMeta

    _valor_da_compra = 0.0

    @abstractmethod
    def exibe_informacao(self):
        pass

    @abstractmethod
    def clonar(self):
        pass

    @property
    def valor_da_compra(self):
        return self._valor_da_compra

    @valor_da_compra.setter
    def valor_da_compra(self, valor_da_compra):
        self._valor_da_compra = valor_da_compra
