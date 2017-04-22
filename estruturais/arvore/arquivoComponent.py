from abc import ABCMeta, abstractmethod

class ArquivoComponent(object):

    __metaclass__ = ABCMeta

    nome_do_arquivo = ''

    def imprime_nome_do_arquivo(self):
        print(self.nome_do_arquivo)

    def pega_nome_do_arquivo(self):
        return self.nome_do_arquivo

    def adiciona(self, novo_arquivo):
        raise NameError('Não pode inserir arquivos em: ' + self.nome_do_arquivo + ', pois ele não é uma pasta')

    def remove(self, nome_do_arquivo):
        raise NameError('Não pode remover arquivos em:', self.nome_do_arquivo, ', pois ele não é uma pasta')

    def pega_arquivo(self):
        raise NameError('Não pode pesquisar arquivos em:', self.nome_do_arquivo, ', pois ele não é uma pasta')
