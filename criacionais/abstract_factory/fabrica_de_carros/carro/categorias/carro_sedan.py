from abc import ABC, abstractmethod


class CarroSedan(ABC):
    """
    Classe abstrata responsavel por mostrar informações de carros sedans
    """

    @abstractmethod
    def mostra_informacao(self):
        """
        Mostra informações
        """

        pass
