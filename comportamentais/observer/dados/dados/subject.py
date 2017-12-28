class Subject(object):
    """
    Classe responsavel por gerênciar os observadores.
    """

    def __init__(self, observadores=[]):
        """
        Inicializa os observadores.
        """

        self.observadores = observadores

    def adiciona_observador(self, observador):
        """
        Adiciona um observador a lista.
        """

        self.observadores.append(observador)

    def remove_observador(self, indice):
        """
        Remove um observador da lista.
        """

        self.observadores.remove(indice)

    def modifica_estado(self, dados):
        """
        Modifica o estado dos dados sendo observados.
        """

        self.dados = dados
        self.notifica_observadores()

    def notifica_observadores(self):
        """
        Notifica os observadores de possiveis modificações nos dados.
        """

        for observador in self.observadores:
            observador.atualiza()

    def pega_estado(self):
        """
        Pega o estado atual dos dados.
        """

        return self.dados
