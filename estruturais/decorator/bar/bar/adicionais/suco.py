from bar.coquetel_decorator import CoquetelDecorator


class Suco(CoquetelDecorator):
    """
    Adicional suco.
    """

    def __init__(self, coquetel):
        """
        Cria um adicional para o coquetel.
        """

        # Passa o coquetel para o contrutor do decorator
        super().__init__(coquetel)

        # Dados do adicional
        self.nome = "Suco"
        self.preco = 2.0
