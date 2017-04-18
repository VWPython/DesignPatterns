from carro.fabricas.fabricaDeCarros import FabricaDeCarros
from carro.modelos.celta import Celta

class Chevrolet(FabricaDeCarros):

    def constroi_carro(self):
        return Celta()
