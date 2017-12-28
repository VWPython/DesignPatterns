from bar.coquetelDecorator import CoquetelDecorator


class Suco(CoquetelDecorator):

    def __init__(self, coquetel):
        """
        Cria um adicional para o coquetel.
        """

        # Passa o coquetel para o contrutor do decorator
        super().__init__(coquetel)

        # Dados do adicional
        self.nome = "Suco"
        self.preco = 2.0
