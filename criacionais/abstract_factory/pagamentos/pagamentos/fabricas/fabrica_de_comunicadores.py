from pagamentos.comunicadores import FabricaDeComunicadores
from pagamentos.fabricas.fabrica_de_emissores import FabricaDeEmissores
from pagamentos.fabricas.fabrica_de_receptores import FabricaDeReceptores


class FabricaDeComunicadoresVisa(FabricaDeComunicadores):

    def __init__(self):
        self.__fabrica_de_emissores = FabricaDeEmissores()
        self.__fabrica_de_receptores = FabricaDeReceptores()

    def cria_emissor(self):
        return self.__fabrica_de_emissores.cria(FabricaDeEmissores.VISA)

    def cria_receptor(self):
        return self.__fabrica_de_receptores.cria(FabricaDeReceptores.VISA)


class FabricaDeComunicadoresMasterCard(FabricaDeComunicadores):

    def __init__(self):
        self.__fabrica_de_emissores = FabricaDeEmissores()
        self.__fabrica_de_receptores = FabricaDeReceptores()

    def cria_emissor(self):
        return self.__fabrica_de_emissores.cria(FabricaDeEmissores.MASTERCARD)

    def cria_receptor(self):
        return self.__fabrica_de_receptores.cria(FabricaDeReceptores.MASTERCARD)
