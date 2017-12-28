from bar.coquetel import Coquetel


class Cachaca(Coquetel):
    """
    Coquetel Cachaça.
    """

    def __init__(self):
        """
        Nome e preço da cachaça.
        """

        self.nome = "Cachaça"
        self.preco = 1.5
