from carro.fabricas.fabricaDeCarros import FabricaDeCarros
from carro.modelos.fiesta import Fiesta

class Ford(FabricaDeCarros):

    def constroi_carro(self):
        return Fiesta()
