from abc import ABC, abstractmethod


class FabricaDeComunicadores(ABC):
    """
    Classe abstrata que serve como template para criar comunicadores.
    """

    @abstractmethod
    def cria_emissor(self):
        """
        Método que deve ser implementado para criar um emissor.
        """

        pass

    @abstractmethod
    def cria_receptor(self):
        """
        Método que deve ser implementado para criar um receptor
        """

        pass
