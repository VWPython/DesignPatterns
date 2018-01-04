from imagem.apis import OpenGLImage
from imagem.imagem_target import ImagemTarget


class OpenGLImageAdapter(OpenGLImage, ImagemTarget):
    """
    Adaptador da API OpenGL.
    """

    def carrega_imagem(self, arquivo):
        """
        Carrega imagem da API OpenGL
        """

        self.gl_carrega_imagem(arquivo)

    def desenha_imagem(self, posX, posY, largura, altura):
        """
        Desenha imagem da API OpenGL
        """

        self.gl_desenha_imagem(posX, posY)
