from bar.coquetelDecorator import CoquetelDecorator


class Limao(CoquetelDecorator):

    def __init__(self, coquetel):
        """
        Cria um adicional para o coquetel.
        """

        # Passa o coquetel para o contrutor do decorator
        super().__init__(coquetel)

        # Dados do adicional
        self.nome = "Limão"
        self.preco = 0.75
