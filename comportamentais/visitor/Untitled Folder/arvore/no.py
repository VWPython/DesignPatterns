class No(object):

    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

    def to_string(self):
        return str(self.chave)

    def pega_chave(self):
        return self.chave

    def pega_no_esquerda(self):
        return self.esquerda

    def modifica_no_esquerda(self, no_esquerdo):
        self.esquerda = no_esquerdo

    def pega_no_direita(self):
        return self.direita

    def modifica_no_direita(self, no_direito):
        self.direito = no_direito
