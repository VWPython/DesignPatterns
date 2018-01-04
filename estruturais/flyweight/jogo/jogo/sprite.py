from jogo.sprite_flyweight import SpriteFlyweight
from jogo.imagem import Imagem


class Sprite(SpriteFlyweight):
    """
    Sprite ou conjunto de imagens em uma única imagem.
    """

    def __init__(self, nome_da_imagem):
        """
        Constroi a sprite.
        """

        self.imagem = Imagem(nome_da_imagem)

    def desenha_imagem(self, ponto):
        """
        Desenha as imagens nos pontos ou coordenadas especificas.
        """

        self.imagem.desenha_imagem()

        print("No ponto ({0}, {1})!".format(
            str(ponto.posX),
            str(ponto.posY)
        ))
