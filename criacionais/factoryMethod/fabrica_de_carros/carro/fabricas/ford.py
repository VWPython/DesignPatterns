from carro.fabricas.fabricaDeCarros import FabricaDeCarros
from carro.modelos.ford import Fiesta, Ka, Ecosport


class Ford(FabricaDeCarros):

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
