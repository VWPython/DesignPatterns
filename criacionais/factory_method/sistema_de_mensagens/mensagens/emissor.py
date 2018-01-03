from abc import ABC, abstractmethod


class Emissor(ABC):
    """
    Classe abstrata para criar emissores.
    """

    @abstractmethod
    def envia(self, mensagem):
        """
        Envia mensagem.
        """

        pass
