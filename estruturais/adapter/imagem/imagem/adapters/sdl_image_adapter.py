from imagem.apis import SDLSurface
from imagem.imagem_target import ImagemTarget


class SDLImageAdapter(SDLSurface, ImagemTarget):
    """
    Adaptador da API SDLImagem
    """

    def carrega_imagem(self, arquivo):
        """
        Carrega imagem da API SDLImagem
        """

        self.sdl_carrega_surface(arquivo)

    def desenha_imagem(self, posX, posY, largura, altura):
        """
        Desenha imagem da API SDLImagem
        """

        self.sql_desenha_surface(largura, altura, posX, posY)
