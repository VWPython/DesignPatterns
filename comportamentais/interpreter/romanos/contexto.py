class Contexto(object):

    output = 0
    input = ''

    def __init__(self, contexto_input):
        self.input = contexto_input

    def pega_input(self):
        return self.input

    def modifica_input(self, contexto_input):
        self.input = contexto_input

    def pega_output(self):
        return self.output

    def modifica_output(self, contexto_output):
        self.output = contexto_output
