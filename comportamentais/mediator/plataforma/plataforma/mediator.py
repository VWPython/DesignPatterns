from abc import ABC, abstractmethod


class Mediator(ABC):
    """
    Interface que padroniza as operações que serão chamadas pelas plataformas.
    """

    @abstractmethod
    def envia(mensagem, plataforma):
        """
        Envia a mensagem para alguma plataforma especifica.
        """

        pass
