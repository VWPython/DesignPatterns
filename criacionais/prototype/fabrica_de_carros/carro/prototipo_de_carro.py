from abc import ABC, abstractmethod


class PrototipoDeCarro(ABC):
    """
    Classe abstrata que serve como template para criar prótotipos de carros.
    """

    def __init__(self):
        """
        Inicializa o valor de compra do carro.
        """

        self.__valor_da_compra = 0.0

    @abstractmethod
    def exibe_informacao(self):
        """
        Exibe informações do carro.
        """

        pass

    @abstractmethod
    def clonar(self):
        """
        Cria uma cópia do carro.
        """

        pass

    @property
    def valor_da_compra(self):
        """
        Pega o valor de compra do carro.
        """

        return self.__valor_da_compra

    @valor_da_compra.setter
    def valor_da_compra(self, valor_da_compra):
        """"
        Modifica o valor de compra do carro.
        """

        self.__valor_da_compra = valor_da_compra
