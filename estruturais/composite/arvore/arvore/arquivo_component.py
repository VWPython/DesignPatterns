from abc import ABC


class ArquivoComponent(ABC):
    """
    Classe abstrata  responsavel por criar componentes ou arquivos.
    """

    def __init__(self, titulo):
        """
        Controi o arquivo de video.
        """

        self.titulo = titulo

    def mostra(self):
        """
        Imprime o nome do arquivo
        """

        print(self.titulo)

    def adiciona(self, arquivo):
        """
        Adiciona o arquivo
        """

        print(
            'Não pode inserir arquivos em: {0}, pois ele não é uma pasta'
            .format(self.titulo)
        )

    def remove(self, titulo):
        """
        Remove o arquivo
        """

        print(
            'Não pode remover arquivos em: {0}, pois ele não é uma pasta'
            .format(self.titulo)
        )

    def pega(self, titulo):
        """
        Pega o arquivo.
        """

        print(
            'Não pode pesquisa arquivos em: {0}, pois ele não é uma pasta'
            .format(self.titulo)
        )
