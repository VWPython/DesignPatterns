from abc import ABC, abstractmethod


class Carro(ABC):
    """
    Classe abstrata para criação de carros.
    """

    @abstractmethod
    def mostra_informacao(self):
        """
        Mostra informações do carro.
        """

        pass
