from abc import ABC, abstractmethod


class Trecho(ABC):
    """
    Classe abstrata que serve de template para a construção de trechos.
    """

    @abstractmethod
    def imprime(self):
        """
        Imprime um trecho.
        """

        pass
