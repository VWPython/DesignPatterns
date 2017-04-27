from canal.iteradorInterface import IteradorInterface

class IteradorMatrizDeCanais(IteradorInterface):

    lista = []
    contador = 0

    def __init__(self, lista):
        self.lista = lista
        self.contador = 0

    def first(self):
        self.contador = 0

    def next(self):
        self.contador += 1

    def is_done(self):
        if(self.contador == len(self.lista)):
            return True
        else:
            return False

    def current_item(self):
        if(self.is_done()):
            self.contador = len(self.lista) - 1
        elif self.contador < 0:
            self.contador = 0
        return self.lista[self.contador]
