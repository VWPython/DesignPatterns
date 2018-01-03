from carro.categorias.carro_popular import CarroPopular


class Palio(CarroPopular):
    """
    Carro popular Palio.
    """

    def mostra_informacao(self):
        """
        Mostra informações do palio.
        """

        print("Modelo: Palio")
        print("Fabricante: Fiat")
        print("Categoria: Popular\n")


class Uno(CarroPopular):
    """
    Carro popular Uno.
    """

    def mostra_informacao(self):
        """
        Mostrar informações do Uno
        """

        print("Modelo: Uno")
        print("Fabricante: Fiat")
        print("Categoria: Popular\n")


class Fiesta(CarroPopular):
    """
    Carro popular Fiesta.
    """

    def mostra_informacao(self):
        """
        Mostrar informações do Fiesta.
        """

        print("Modelo: Fiesta")
        print("Fabricante: Ford")
        print("Categoria: Popular\n")


class Ka(CarroPopular):
    """
    Carro popular Ka.
    """

    def mostra_informacao(self):
        """
        Mostrar informações do Ka.
        """

        print("Modelo: Ka")
        print("Fabricante: Ford")
        print("Categoria: Popular\n")
