from abc import ABC, abstractmethod


class SpriteFlyweight(ABC):
    """
    Classe abstrata para a criação de sprites
    """

    @abstractmethod
    def desenha_imagem(self, ponto):
        """
        Desenha a imagem inserindo suas coordenadas
        """

        pass
