from trecho.trecho import Trecho


class Carro(Trecho):
    """
    Trecho de carro.
    """

    def __init__(self, direcao, distancia):
        """
        Constroi um trecho.
        """

        self.direcao = direcao
        self.distancia = distancia

    def imprime(self):
        """
        Imprime o trecho.
        """

        print("\nVá de carro: ")
        print(self.direcao)
        print("A distância percorrida será de %d metros" % self.distancia)
