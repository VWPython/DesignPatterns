from abc import ABC, abstractmethod


class Comando(ABC):
    """
    Classe abstrata para criar um comando.
    """

    @abstractmethod
    def executa(self):
        """
        Executa o comando.
        """

        pass
