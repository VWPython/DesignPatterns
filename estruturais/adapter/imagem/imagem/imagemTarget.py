from abc import ABC, abstractmethod


class ImagemTarget(ABC):

    @abstractmethod
    def carrega_imagem(self, arquivo):
        pass

    @abstractmethod
    def desenha_imagem(self, posX, posY, largura, altura):
        pass
