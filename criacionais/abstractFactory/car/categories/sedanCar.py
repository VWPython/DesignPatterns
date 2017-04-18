from abc import ABCMeta, abstractmethod

class SedanCar(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def show_information(self):
        pass
