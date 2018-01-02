from abc import ABC, abstractmethod


class Comando(ABC):
    """
    Classe abstrata para criar comandos do tocador de música.
    """

    @abstractmethod
    def executa(self):
        """
        Executa o comando.
        """

        pass
