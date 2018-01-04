from abc import ABC


class Coquetel(ABC):
    """
    Classe abstrada de coqueteis.
    """

    def get_nome(self):
        """
        Pega o nome do coquetel.
        """

        return self.nome

    def get_preco(self):
        """
        Pega o preço do coquetel
        """

        return self.preco
