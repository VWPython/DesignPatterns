from carro.fabricas.fabricaDeCarros import FabricaDeCarros
from carro.modelos.palio import Palio

class Fiat(FabricaDeCarros):

    def constroi_carro(self):
        return Palio()
