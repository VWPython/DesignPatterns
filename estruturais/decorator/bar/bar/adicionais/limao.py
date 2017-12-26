from bar.coquetelDecorator import CoquetelDecorator

class Limao(CoquetelDecorator):

    def __init__(self, coquetel):
        super().__init__(coquetel)
        self.nome = "Limão"
        self.preco = 0.75
