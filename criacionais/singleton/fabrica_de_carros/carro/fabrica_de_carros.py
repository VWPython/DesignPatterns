class FabricaDeCarros(object):
    """
    Fabrica de carros.
    """

    total_de_carros_fiat = 0
    total_de_carros_ford = 0
    total_de_carros_volks = 0

    # Instancia privada
    __instancia = None

    def __init__(self):
        """
        Se a instância já existir mostre uma mensagem.
        """

        if self.__instancia is not None:
            raise ValueError("O objeto já existe! utilize a função pega_instancia()")

    def cria_carro_volks(self):
        """
        Cria um carro da volks.
        """

        self.total_de_carros_volks += 1
        print("Carro Volks #", self.total_de_carros_volks, " criado")

    def cria_carro_ford(self):
        """
        Cria um carro da ford.
        """

        self.total_de_carros_ford += 1
        print("Carro Ford #", self.total_de_carros_ford, " criado")

    def cria_carro_fiat(self):
        """
        Cria um carro da fiat.
        """

        self.total_de_carros_fiat += 1
        print("Carro Fiat #", self.total_de_carros_fiat, " criado")

    def gera_relatorio(self):
        """
        Gera o relatória de carros vendidos
        """

        print("Total de carros Fiat vendidos:", self.total_de_carros_fiat)
        print("Total de carros Ford vendidos:", self.total_de_carros_ford)
        print("Total de carros Volks vendidos:", self.total_de_carros_volks)

    @staticmethod
    def pega_instancia():
        """
        Pega a instância da fábrica..
        """

        if(FabricaDeCarros.__instancia is None):
            FabricaDeCarros.__instancia = FabricaDeCarros()
        return FabricaDeCarros.__instancia
