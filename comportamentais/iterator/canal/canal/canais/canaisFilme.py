from canal.agregadoDeCanais import AgregadoDeCanais
from canal.iteradores.iteradorMatrizDeCanais import IteradorMatrizDeCanais

class CanaisFilme(AgregadoDeCanais):

    # Finge que e outro tipo de lista
    canais = []

    def __init__(self):
        self.canais.append("Netflix")
        self.canais.append("Filmes online")
        self.canais.append("Tela quente")
        self.canais.append("Sessão da tarde")

    def criar_iterador(self):
        return IteradorMatrizDeCanais(self.canais)
