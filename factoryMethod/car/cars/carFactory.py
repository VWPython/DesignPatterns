from abc import ABCMeta, abstractmethod

class Car(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def show_information(self):
        pass
