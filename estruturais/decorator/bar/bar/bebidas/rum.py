from bar.coquetel import Coquetel


class Rum(Coquetel):
    """
    Coquetel RUM.
    """

    def __init__(self):
        """
        Nome e preço do RUM.
        """

        self.nome = "Rum"
        self.preco = 2.35
