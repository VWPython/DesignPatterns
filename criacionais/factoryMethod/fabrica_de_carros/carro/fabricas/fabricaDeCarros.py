from abc import ABCMeta, abstractmethod

class FabricaDeCarros(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def constroi_carro(self):
        pass
