from carro.fabricas.fabricaDeCarros import FabricaDeCarros
from carro.modelos.sedan import FiestaSedan, KaSedan
from carro.modelos.popular import Fiesta, Ka


class Ford(FabricaDeCarros):

    FIESTA = 0
    KA = 1
    FIESTA_SEDAN = 2
    KA_SEDAN = 3

    def constroi_carro_sedan(self, modelo):
        if modelo == self.FIESTA_SEDAN:
            return FiestaSedan()
        elif modelo == self.KA_SEDAN:
            return KaSedan()

    def constroi_carro_popular(self, modelo):
        if modelo == self.FIESTA:
            return Fiesta()
        elif modelo == self.KA:
            return Ka()
