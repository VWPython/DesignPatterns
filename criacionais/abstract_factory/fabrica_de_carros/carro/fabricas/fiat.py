from carro.fabricas.fabrica_de_carros import FabricaDeCarros
from carro.modelos.sedan import Siena, Weekend
from carro.modelos.popular import Palio, Uno


class Fiat(FabricaDeCarros):
    """
    Fabrica de carros da Fiat.
    """

    PALIO = 0
    UNO = 1
    SIENA = 3
    WEEKEND = 4

    def constroi_carro_sedan(self, modelo):
        """
        Constroi carros sedans da fiat.
        """

        if modelo == self.SIENA:
            return Siena()
        elif modelo == self.WEEKEND:
            return Weekend()

    def constroi_carro_popular(self, modelo):
        """
        Constroi carros populares da fiat.
        """

        if modelo == self.UNO:
            return Uno()
        elif modelo == self.PALIO:
            return Palio()
