from musica.comando import Comando


class AumentarVolume(Comando):
    """
    Comando de aumentar o volume da música.
    """

    def __init__(self, player, intensidade):
        """
        Constroi o comando.
        """

        self.player = player
        self.intensidade = intensidade

    def executa(self):
        """
        Executa o comando para aumentar o volume da música.
        """

        self.player.aumentar_volume(self.intensidade)
