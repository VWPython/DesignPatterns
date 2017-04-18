class FabricaDeCarros(object):
    total_de_carros_fiat = 0
    total_de_carros_ford = 0
    total_de_carros_volks = 0
    __instancia = None

    def __init__(self):
        if self.__instancia is not None:
            raise ValueError("O objeto já existe! utilize a função pega_instancia()")

    def cria_carro_volks(self):
        self.total_de_carros_volks += 1
        print("Carro Volks #", self.total_de_carros_volks, " criado")

    def cria_carro_ford(self):
        self.total_de_carros_ford += 1
        print("Carro Ford #", self.total_de_carros_ford, " criado")

    def cria_carro_fiat(self):
        self.total_de_carros_fiat += 1
        print("Carro Fiat #", self.total_de_carros_fiat, " criado")

    def gera_relatorio(self):
        print("Total de carros Fiat vendidos:", self.total_de_carros_fiat)
        print("Total de carros Ford vendidos:", self.total_de_carros_ford)
        print("Total de carros Volks vendidos:", self.total_de_carros_volks)

    def pega_instancia():
        if(FabricaDeCarros.__instancia is None):
            FabricaDeCarros.__instancia = FabricaDeCarros()
        return FabricaDeCarros.__instancia
