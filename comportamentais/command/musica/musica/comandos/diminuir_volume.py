from musica.comando import Comando


class DiminuirVolume(Comando):
    """
    Comando de diminuir o volume da música.
    """

    def __init__(self, player, intensidade):
        """
        Constroi o comando.
        """

        self.player = player
        self.intensidade = intensidade

    def executa(self):
        """
        Executa o comando para diminuir o volume da música.
        """

        self.player.diminuir_volume(self.intensidade)
