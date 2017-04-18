from carro.fabricas.fabricaDeCarros import FabricaDeCarros
from carro.modelos.siena import Siena
from carro.modelos.palio import Palio

class Fiat(FabricaDeCarros):

    def constroi_carro_sedan(self):
        return Siena()

    def constroi_carro_popular(self):
        return Palio()
