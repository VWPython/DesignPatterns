from bar.coquetelDecorator import CoquetelDecorator

class Acuca(CoquetelDecorator):

    def __init__(self, coquetel):
        super().__init__(coquetel)
        self.nome = "Açucar"
        self.preco = 0.50
