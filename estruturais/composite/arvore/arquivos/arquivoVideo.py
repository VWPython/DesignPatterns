from arvore.arquivoComponent import ArquivoComponent

class ArquivoVideo(ArquivoComponent):

    nome_do_arquivo = ''

    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
