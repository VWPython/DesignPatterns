from abc import ABC, abstractmethod


class Imposto(ABC):
    """
    Classe abstrata de imposto.
    """

    def __init__(self, outro_imposto=None):
        """
        Constroi impostos sobre impostos de maneira dinamica.
        """

        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        """
        Calculo dos impostos aninhados.
        """

        if self.__outro_imposto is None:
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        """
        Calcula o imposto.
        """

        pass
