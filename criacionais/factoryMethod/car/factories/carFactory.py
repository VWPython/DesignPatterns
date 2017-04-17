from abc import ABCMeta, abstractmethod

class CarFactory(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def build_car(self):
        pass
