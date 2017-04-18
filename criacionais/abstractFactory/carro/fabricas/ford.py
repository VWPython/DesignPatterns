from carro.fabricas.fabricaDeCarros import FabricaDeCarros
from carro.modelos.fiestaSedan import FiestaSedan
from carro.modelos.fiesta import Fiesta

class Ford(FabricaDeCarros):

    def constroi_carro_sedan(self):
        return FiestaSedan()

    def constroi_carro_popular(self):
        return Fiesta()
