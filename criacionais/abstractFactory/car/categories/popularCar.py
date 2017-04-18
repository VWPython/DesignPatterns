from abc import ABCMeta, abstractmethod

class PopularCar(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def show_information(self):
        pass
