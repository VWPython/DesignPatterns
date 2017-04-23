from bar.coquetelDecorator import CoquetelDecorator

class Refrigerante(CoquetelDecorator):

    def __init__(self, coquetel):
        super().__init__(coquetel)
        self.nome = "Refrigerante"
        self.preco = 1.0
