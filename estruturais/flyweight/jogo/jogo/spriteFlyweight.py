from abc import ABC, abstractmethod

class SpriteFlyweight(ABC):

    @abstractmethod
    def desenha_imagem(self, ponto):
        pass
