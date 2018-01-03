from abc import ABC, abstractmethod
from carro.produto import Carro


class FabricaDeCarros(ABC):
    """
    Classe abstrata que funciona como um template para criação
    de fábricas de carro.
    """

    def __init__(self):
        """
        Pega o modelo do carro.
        """

        self.carro = Carro()

    @abstractmethod
    def define_preco(self, preco):
        """
        Define o preço do carro.
        """

        pass

    @abstractmethod
    def define_motor(self, motor):
        """
        Define o motor do carro.
        """

        pass

    @abstractmethod
    def define_ano_de_fabricacao(self, ano_de_fabricacao):
        """
        Define o ano de fabricação do carro.
        """

        pass

    @abstractmethod
    def define_modelo(self, modelo):
        """
        Define o modelo do carro.
        """

        pass

    @abstractmethod
    def define_montadora(self):
        """
        Define a montadora do carro.
        """

        pass

    def constroi_carro(self):
        """
        Constroi o carro.
        """

        return self.carro
