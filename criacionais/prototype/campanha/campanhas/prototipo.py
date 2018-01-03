from abc import ABC, abstractmethod


class Prototipo(ABC):
    """
    Classe abstrata que serve como template para classes que querem
    clonar suas intâncias.
    """

    @abstractmethod
    def clone(self):
        """
        Clona instância.
        """

        pass
