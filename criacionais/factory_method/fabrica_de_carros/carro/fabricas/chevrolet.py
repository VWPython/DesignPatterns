from carro.fabricas.fabrica_de_carros import FabricaDeCarros
from carro.modelos.chevrolet import Celta, Prisma, Onix


class Chevrolet(FabricaDeCarros):

    ONIX = 0
    CELTA = 1
    PRISMA = 2

    def constroi_carro(self, modelo):
        if modelo == self.ONIX:
            return Onix()
        elif modelo == self.CELTA:
            return Celta()
        elif modelo == self.PRISMA:
            return Prisma()
