from abc import ABC, abstractmethod


class ImagemTarget(ABC):
    """
    Interface em comum para a adaptação.
    """

    @abstractmethod
    def carrega_imagem(self, arquivo):
        """
        Carrega a imagem.
        """

        pass

    @abstractmethod
    def desenha_imagem(self, posX, posY, largura, altura):
        """
        Desenha a imagem
        """

        pass
