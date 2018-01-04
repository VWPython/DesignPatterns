from arvore.arquivo_component import ArquivoComponent


class ArquivoComposite(ArquivoComponent):
    """
    Composição de arquivos, ou pasta.
    """

    arquivos = []

    def __init__(self, titulo):
        """
        Define o nome da pasta e cria ela.
        """

        super(ArquivoComposite, self).__init__(titulo)

    def mostra(self):
        """
        Imprime o nome da pasta.
        """

        print(self.titulo)

        for arquivo in self.arquivos:
            arquivo.mostra()

    def adiciona(self, arquivo):
        """
        Adiciona o arquivo na pasta.
        """

        self.arquivos.append(arquivo)

    def remove(self, titulo):
        """
        Remove o arquivo da pasta
        """

        for arquivo in self.arquivos:
            if(arquivo.titulo == titulo):
                self.arquivos.remove(arquivo)
                return

        print('Não existe esse arquivo!')

    def pega(self, titulo):
        """
        Pega o arquivo dentro da pasta.
        """

        for arquivo in self.arquivos:
            if(arquivo.titulo == titulo):
                return arquivo

        print('Não existe esse arquivo!')
