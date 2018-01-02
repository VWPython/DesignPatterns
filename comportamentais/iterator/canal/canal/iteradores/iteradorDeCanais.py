from canal.iteradorInterface import IteradorInterface


class IteradorDeCanais(IteradorInterface):
    """
    Classe que irá iterar entre as listas de canais disponíveis
    """

    lista = []
    contador = 0

    def __init__(self, lista):
        """
        Cria o iterador com a lista de canais.
        """

        self.lista = lista
        self.contador = 0

    def primeiro(self):
        """
        Pega o primeiro canal da lista.
        """

        self.contador = 0

    def proximo(self):
        """
        Pega o próximo canal da lista.
        """

        self.contador += 1

    def acabou(self):
        """
        Verifica se o iterador já percorreu todos os canais da lista.
        """

        if(self.contador == len(self.lista)):
            return True
        else:
            return False

    def canal_atual(self):
        """
        Pega o canal atual da lista.
        """

        if(self.acabou()):
            self.contador = len(self.lista) - 1
        elif self.contador < 0:
            self.contador = 0

        return self.lista[self.contador]
