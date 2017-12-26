from jogo.spriteFlyweight import SpriteFlyweight
from jogo.imagem import Imagem

class Sprite(SpriteFlyweight):
    imagem = None

    def __init__(self, nome_da_imagem):
        self.imagem = Imagem(nome_da_imagem)

    def desenha_imagem(self, ponto):
        self.imagem.desenha_imagem()
        print("No ponto (" + str(ponto.posX) + ", " + str(ponto.posY) + ")!")
