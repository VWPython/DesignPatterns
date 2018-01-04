class Imagem(object):
    """
    Imagem das sprints.
    """

    def __init__(self, nome_da_imagem):
        """
        Construtor da imagem.
        """

        self.nome_da_imagem = nome_da_imagem

    def desenha_imagem(self):
        """
        Desenha a imagem.
        """

        print(self.nome_da_imagem + " desenhada!")
