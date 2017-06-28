from abc import ABCMeta, abstractmethod

class Carro(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def mostra_informacao(self):
        pass
