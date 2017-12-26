class TextoMemento(object):

    def __init__(self, texto):
        self.estado_do_texto = texto

    def pega_texto_salvo(self):
        return self.estado_do_texto
