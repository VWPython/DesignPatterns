from musica.comando import Comando


class Tocar(Comando):
    """
    Comando de tocar a música.
    """

    def __init__(self, player, arquivo):
        """
        Constroi o comando.
        """

        self.player = player
        self.arquivo = arquivo

    def executa(self):
        """
        Executa o comando para tocar a música.
        """

        self.player.play(self.arquivo)
