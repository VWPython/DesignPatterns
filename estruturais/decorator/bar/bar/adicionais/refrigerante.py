from bar.coquetel_decorator import CoquetelDecorator


class Refrigerante(CoquetelDecorator):
    """
    Adicional refrigerante
    """

    def __init__(self, coquetel):
        """
        Cria um adicional para o coquetel.
        """

        # Passa o coquetel para o contrutor do decorator
        super().__init__(coquetel)

        # Dados do adicional
        self.nome = "Refrigerante"
        self.preco = 1.0
