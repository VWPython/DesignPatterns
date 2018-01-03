from abc import ABC, abstractmethod


class Receptor(ABC):
    """
    Classe abstrata que server como template para criar receptores de mensagem.
    """

    @abstractmethod
    def recebe(self):
        """
        Método de receber mensagem que deve ser implementado.
        """

        pass
