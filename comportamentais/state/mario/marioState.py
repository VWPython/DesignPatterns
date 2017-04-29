from abc import ABC, abstractmethod

class MarioState(ABC):

    @abstractmethod
    def pega_cogumelo(self):
        pass

    @abstractmethod
    def pega_flor(self):
        pass

    @abstractmethod
    def pega_pena(self):
        pass

    @abstractmethod
    def leva_dano(self):
        pass
