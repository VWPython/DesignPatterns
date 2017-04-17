from abc import ABCMeta, abstractmethod

class Emissor(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def envia(mensagem):
        pass
