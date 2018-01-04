from trecho.trecho import Trecho


class Andando(Trecho):
    """
    Trecho andando.
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

        print("\nVá andando: ")
        print(self.direcao)
        print("A distância percorrida será de %d metros" % self.distancia)
