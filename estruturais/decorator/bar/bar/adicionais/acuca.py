from bar.coquetel_decorator import CoquetelDecorator


class Acuca(CoquetelDecorator):
    """
    Adicional açucar
    """

    def __init__(self, coquetel):
        """
        Cria um adicional para o coquetel.
        """

        # Passa o coquetel para o contrutor do decorator
        super().__init__(coquetel)

        # Dados do adicional
        self.nome = "Açucar"
        self.preco = 0.50
