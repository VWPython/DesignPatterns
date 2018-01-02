from canal.agregadoDeCanais import AgregadoDeCanais
from canal.iteradores.iteradorDeCanais import IteradorDeCanais


class Esporte(AgregadoDeCanais):
    """
    Canais de esporte.
    """

    canais = []

    def __init__(self):
        """
        Cria o canal de esportes com todo o seu conteúdo.
        """

        self.canais.append("Esporte ao vivo")
        self.canais.append("Basquete 2011")
        self.canais.append("Campeonato Italiano")
        self.canais.append("Campeonato Espanhol")
        self.canais.append("Campeonato Brasileiro")

    def criar_iterador(self):
        """
        Insere o canal de esportes no iterador de canais
        """

        return IteradorDeCanais(self.canais)
