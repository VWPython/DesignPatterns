from abc import ABC, abstractmethod


class CarroPopular(ABC):
    """
    Classe abstrata responsavel por mostrar informações de carros populares.
    """

    @abstractmethod
    def mostra_informacao(self):
        """
        Mostra informação do carro.
        """

        pass
