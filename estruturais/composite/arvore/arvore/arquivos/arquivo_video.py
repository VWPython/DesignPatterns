from arvore.arquivo_component import ArquivoComponent


class ArquivoVideo(ArquivoComponent):
    """
    Arquivo de video.
    """

    def __init__(self, titulo):
        """
        Controi o arquivo de video.
        """

        super(ArquivoVideo, self).__init__(titulo)
