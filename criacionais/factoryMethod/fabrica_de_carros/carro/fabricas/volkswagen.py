from carro.fabricas.fabricaDeCarros import FabricaDeCarros
from carro.modelos.gol import Gol

class Volkswagen(FabricaDeCarros):

    def constroi_carro(self):
        return Gol()
