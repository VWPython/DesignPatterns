from carro.fabricas.fabricaDeCarros import FabricaDeCarros
from carro.modelos.volkswagen import Gol, CrossFox, Saveiro


class Volkswagen(FabricaDeCarros):

    GOL = 0
    CROSSFOX = 1
    SAVEIRO = 2

    def constroi_carro(self, modelo):
        if modelo == self.GOL:
            return Gol()
        elif modelo == self.CROSSFOX:
            return CrossFox()
        elif modelo == self.SAVEIRO:
            return Saveiro()
