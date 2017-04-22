from arvore.arquivoComponent import ArquivoComponent

class ArquivoComposite(ArquivoComponent):

    arquivos = []
    nome_do_arquivo = ''

    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo

    def imprime_nome_do_arquivo(self):
        print(self.nome_do_arquivo)
        for arquivo in self.arquivos:
            arquivo.imprime_nome_do_arquivo()

    def pega_nome_do_arquivo(self):
        return self.nome_do_arquivo

    def adiciona(self, novo_arquivo):
        self.arquivos.append(novo_arquivo)

    def remove(self, nome_do_arquivo):
        for arquivo in self.arquivos:
            if(arquivo.pega_nome_do_arquivo() == nome_do_arquivo):
                self.arquivos.remove(arquivo)
                return;
        raise NameError('Não existe esse arquivo!')

    def pega_arquivo(self, nome_do_arquivo):
        for arquivo in self.arquivos:
            if(arquivo.pega_nome_do_arquivo() == nome_do_arquivo):
                return arquivo
        raise NameError('Não existe esse arquivo!')

