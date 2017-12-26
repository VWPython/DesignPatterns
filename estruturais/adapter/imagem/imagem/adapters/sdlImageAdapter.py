from imagem.apis.sdlSurface import SDLSurface
from imagem.imagemTarget import ImagemTarget

class SDLImageAdapter(SDLSurface, ImagemTarget):

    def carrega_imagem(self, arquivo):
        self.sdl_carrega_surface(arquivo)

    def desenha_imagem(self, posX, posY, largura, altura):
        self.sql_desenha_surface(largura, altura, posX, posY)
