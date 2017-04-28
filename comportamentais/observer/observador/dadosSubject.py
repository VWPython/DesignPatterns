from observador.dados import Dados

class DadosSubject(object):

    def __init__(self, observadores=[]):
        self.observadores = observadores

    def adiciona_observador(self, observador):
        self.observadores.append(observador)

    def remove_observador(self, indice):
        self.observadores.remove(indice)

    def modifica_estado(self, dados):
        self.dados = dados
        self.notifica_observadores()

    def notifica_observadores(self):
        for observador in self.observadores:
            observador.atualiza()

    def pega_estado(self):
        return self.dados
