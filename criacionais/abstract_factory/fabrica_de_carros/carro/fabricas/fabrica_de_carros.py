from abc import ABC, abstractmethod


class FabricaDeCarros(ABC):
    """
    Classe abstrata que servirá de template para criar fabrica de carros.
    """

    @abstractmethod
    def constroi_carro_sedan(self, modelo):
        """
        Método responsavel por construir carros sedans.
        """

        pass

    @abstractmethod
    def constroi_carro_popular(self, modelo):
        """
        Método responsavel por construir carros populares.
        """

        pass
