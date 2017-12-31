from editor.historico import Historico
from editor.estado import Estado


class Texto(object):
    """
    Texto que será escrito.
    """

    def __init__(self):
        """
        Construtor do texto.
        """

        self.historico = Historico()
        self.texto = ''

    def escreve_texto(self, texto):
        """
        Escrever um texto.
        """

        self.historico.adiciona_estado(Estado(texto))

    def desfaze_escrita(self):
        """
        Desfazer a escrita do texto.
        """

        self.estado = self.historico.obtem_ultimo_estado()
        self.texto = self.estado.texto

    def mostra_texto(self):
        """
        Mostrar texto
        """

        print(self.texto)
