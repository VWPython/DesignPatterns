from carro.categorias.carro_sedan import CarroSedan


class Siena(CarroSedan):
    """
    Carro sedan Siena.
    """

    def mostra_informacao(self):
        """
        Mostrar informações do siena.
        """

        print("Modelo: Grand Siena")
        print("Fabricante: Fiat")
        print("Categoria: Sedan\n")


class Weekend(CarroSedan):
    """
    Carro sedan Weekend.
    """

    def mostra_informacao(self):
        """
        Mostrar informações do Weekend.
        """

        print("Modelo: Weekend")
        print("Fabricante: Fiat")
        print("Categoria: Sedan\n")


class FiestaSedan(CarroSedan):
    """
    Carro Fiesta sedan
    """

    def mostra_informacao(self):
        """
        Mostrar informações do fiesta sedan
        """

        print("Modelo: Fiesta Sedan")
        print("Fabricante: Ford")
        print("Categoria: Sedan\n")


class KaSedan(CarroSedan):
    """
    Carro sedan Ka.
    """

    def mostra_informacao(self):
        """
        Mostrar informações do Ka
        """

        print("Modelo: Ka Sedan")
        print("Fabricante: Ford")
        print("Categoria: Sedan\n")
