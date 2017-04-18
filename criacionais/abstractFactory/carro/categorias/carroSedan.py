from abc import ABCMeta, abstractmethod

class CarroSedan(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def mostra_informacao(self):
        pass
