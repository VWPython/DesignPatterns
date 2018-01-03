from abc import ABC, abstractmethod


class Emissor(ABC):
    """
    Classe abstrata utilizada como template para criar emissores de mensagens.
    """

    @abstractmethod
    def envia(self, mensagem):
        """
        Método de enviar mensagem que deve ser implementado.
        """

        pass
