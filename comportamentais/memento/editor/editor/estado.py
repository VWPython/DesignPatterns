class Estado(object):
    """
    Estado do texto.
    """

    def __init__(self, texto):
        """
        Construtor do estado.
        """

        self.__texto = texto

    @property
    def texto(self):
        """
        Pega o texto salvo.
        """

        return self.__texto
