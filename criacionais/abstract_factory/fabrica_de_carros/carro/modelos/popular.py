from carro.categorias.carro_popular import CarroPopular


class Palio(CarroPopular):

    def mostra_informacao(self):
        print("Modelo: Palio")
        print("Fabricante: Fiat")
        print("Categoria: Popular\n")


class Uno(CarroPopular):

    def mostra_informacao(self):
        print("Modelo: Uno")
        print("Fabricante: Fiat")
        print("Categoria: Popular\n")


class Fiesta(CarroPopular):

    def mostra_informacao(self):
        print("Modelo: Fiesta")
        print("Fabricante: Ford")
        print("Categoria: Popular\n")


class Ka(CarroPopular):

    def mostra_informacao(self):
        print("Modelo: Ka")
        print("Fabricante: Ford")
        print("Categoria: Popular\n")
