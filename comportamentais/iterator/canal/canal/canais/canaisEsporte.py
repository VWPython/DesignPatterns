from canal.agregadoDeCanais import AgregadoDeCanais
from canal.iteradores.iteradorListaDeCanais import IteradorListaDeCanais

class CanaisEsporte(AgregadoDeCanais):

    canais = []

    def __init__(self):
        self.canais.append("Esporte ao vivo")
        self.canais.append("Basquete 2011")
        self.canais.append("Campeonato Italiano")
        self.canais.append("Campeonato Espanhol")
        self.canais.append("Campeonato Brasileiro")

    def criar_iterador(self):
        return IteradorListaDeCanais(self.canais)
