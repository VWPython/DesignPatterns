from carro.categorias.carro_sedan import CarroSedan


class Siena(CarroSedan):

    def mostra_informacao(self):
        print("Modelo: Grand Siena")
        print("Fabricante: Fiat")
        print("Categoria: Sedan\n")


class Weekend(CarroSedan):

    def mostra_informacao(self):
        print("Modelo: Weekend")
        print("Fabricante: Fiat")
        print("Categoria: Sedan\n")


class FiestaSedan(CarroSedan):

    def mostra_informacao(self):
        print("Modelo: Fiesta Sedan")
        print("Fabricante: Ford")
        print("Categoria: Sedan\n")


class KaSedan(CarroSedan):

    def mostra_informacao(self):
        print("Modelo: Ka Sedan")
        print("Fabricante: Ford")
        print("Categoria: Sedan\n")
