from imagem.apis.openGLImage import OpenGLImage
from imagem.imagemTarget import ImagemTarget

class OpenGLImageAdapter(OpenGLImage, ImagemTarget):

    def carrega_imagem(self, arquivo):
        self.gl_carrega_imagem(arquivo)

    def desenha_imagem(self, posX, posY, largura, altura):
        self.gl_desenha_imagem(posX, posY)
