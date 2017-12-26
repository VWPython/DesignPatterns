from editor.textoMemento import TextoMemento

class TextoCareTaker(object):

    def __init__(self):
        self.estados = []

    def adiciona_memento(self, memento):
        self.estados.append(memento)

    def pega_ultimo_estado_salvo(self):
        if (len(self.estados) > 0):
            estado_salvo = self.estados[len(self.estados) -1]
            self.estados.pop(len(self.estados) - 1)
            return estado_salvo
        else:
            return TextoMemento("")
