from editor.textoCareTaker import TextoCareTaker
from editor.textoMemento import TextoMemento

class Texto(object):

    def __init__(self):
        self.caretaker = TextoCareTaker()
        self.texto = ''

    def escreve_texto(self, texto):
        self.caretaker.adiciona_memento(TextoMemento(texto))

    def desfaze_escrita(self):
        self.texto = self.caretaker.pega_ultimo_estado_salvo().pega_texto_salvo()

    def mostra_texto(self):
        print(self.texto)
