class Imagem(object):
    nome_da_imagem = ''

    def __init__(self, nome_da_imagem):
        self.nome_da_imagem = nome_da_imagem

    def desenha_imagem(self):
        print(self.nome_da_imagem + " desenhada!")
