from carro.fabricas.fabrica_de_carros import FabricaDeCarros
from carro.modelos.ford import Fiesta, Ka, Ecosport


class Ford(FabricaDeCarros):
    """
    Fabrica de carros da Ford
    """

    KA = 0
    ECOSPORT = 1
    FIESTA = 2

    def constroi_carro(self, modelo):
        if modelo == self.KA:
            return Ka()
        elif modelo == self.ECOSPORT:
            return Ecosport()
        elif modelo == self.FIESTA:
            return Fiesta()
