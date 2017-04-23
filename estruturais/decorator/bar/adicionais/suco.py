from bar.coquetelDecorator import CoquetelDecorator

class Suco(CoquetelDecorator):

    def __init__(self, coquetel):
        super().__init__(coquetel)
        self.nome = "Suco"
        self.preco = 2.0
