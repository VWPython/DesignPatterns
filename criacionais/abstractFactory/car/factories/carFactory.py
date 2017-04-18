from abc import ABCMeta, abstractmethod

class CarFactory(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def build_sendan_car(self):
        pass

    @abstractmethod
    def build_popular_car(self):
        pass
