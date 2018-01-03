from abc import ABC, abstractmethod


class Compartilha(ABC):
    """
    Classe abstrata para construir Objetos compartilhados.
    """

    @abstractmethod
    def adquire(self, numero):
        """
        Adquire um objeto que não esteja sendo utilizado.
        """

        pass

    @abstractmethod
    def libera(self, numero):
        """
        Libera um objeto que está sendo utilizado, para que outros usem.
        """

        pass
