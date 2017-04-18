from abc import ABCMeta, abstractmethod

class FabricaDeCarros(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def constroi_carro_sedan(self):
        pass

    @abstractmethod
    def constroi_carro_popular(self):
        pass
