from abc import ABCMeta, abstractmethod

class CarroPopular(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def mostra_informacao(self):
        pass
