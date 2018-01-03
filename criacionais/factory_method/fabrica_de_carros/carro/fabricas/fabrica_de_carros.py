from abc import ABC, abstractmethod


class FabricaDeCarros(ABC):
    """
    Classe abstrata para a criação de fabrica de carros.
    """

    @abstractmethod
    def constroi_carro(self, modelo):
        """
        Constroi o carro.
        """

        pass
