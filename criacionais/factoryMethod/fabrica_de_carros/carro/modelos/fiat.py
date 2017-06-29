from carro.modelos.carro import Carro


class Palio(Carro):

    def mostra_informacao(self):
        print("Modelo: Palio")
        print("Fabricante: Fiat\n")


class Uno(Carro):

    def mostra_informacao(self):
        print("Modelo: Uno")
        print("Fabricante: Fiat\n")


class Punto(Carro):

    def mostra_informacao(self):
        print("Modelo: Punto")
        print("Fabricante: Fiat\n")
