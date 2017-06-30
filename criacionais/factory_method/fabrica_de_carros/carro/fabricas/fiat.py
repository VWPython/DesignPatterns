from carro.fabricas.fabrica_de_carros import FabricaDeCarros
from carro.modelos.fiat import Palio, Uno, Punto


class Fiat(FabricaDeCarros):

    PALIO = 0
    UNO = 1
    PUNTO = 2

    def constroi_carro(self, modelo):
        if modelo == self.PALIO:
            return Palio()
        elif modelo == self.UNO:
            return Uno()
        elif modelo == self.PUNTO:
            return Punto()
