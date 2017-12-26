class Dados(object):

    def __init__(self, a, b, c):
        self.__valorA = a
        self.__valorB = b
        self.__valorC = c

    @property
    def valorA(self):
        return self.__valorA

    @property
    def valorB(self):
        return self.__valorB

    @property
    def valorC(self):
        return self.__valorC
