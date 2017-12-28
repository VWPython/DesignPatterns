from bar.coquetel import Coquetel


class Vodka(Coquetel):
    """
    Coquetel Vodka.
    """

    def __init__(self):
        """
        Nome e preço da vodka.
        """

        self.nome = "Vodka"
        self.preco = 5.0
