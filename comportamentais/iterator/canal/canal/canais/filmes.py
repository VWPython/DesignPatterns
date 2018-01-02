from canal.agregadoDeCanais import AgregadoDeCanais
from canal.iteradores.iteradorDeCanais import IteradorDeCanais


class Filme(AgregadoDeCanais):
    """
    Canais de filme.
    """

    # Finge que e outro tipo de lista
    canais = []

    def __init__(self):
        """
        Cria o canal de filmes com todo o seu conteúdo.
        """

        self.canais.append("Netflix")
        self.canais.append("Filmes online")
        self.canais.append("Tela quente")
        self.canais.append("Sessão da tarde")

    def criar_iterador(self):
        """
        Insere o canal de filmes no iterador de canais
        """

        return IteradorDeCanais(self.canais)
