from pagamentos.comunicadores import FabricaDeComunicadores
from pagamentos.fabricas import FabricaDeEmissores, FabricaDeReceptores


class FabricaDeComunicadoresVisa(FabricaDeComunicadores):
    """
    Fabrica de comunicadores da Visa.
    """

    def __init__(self):
        """
        Cria as fabricas de emissores e receptores.
        """

        self.__fabrica_de_emissores = FabricaDeEmissores()
        self.__fabrica_de_receptores = FabricaDeReceptores()

    def cria_emissor(self):
        """
        Cria o emissor da visa.
        """

        return self.__fabrica_de_emissores.cria(FabricaDeEmissores.VISA)

    def cria_receptor(self):
        """
        Cria o receptor da visa.
        """

        return self.__fabrica_de_receptores.cria(FabricaDeReceptores.VISA)


class FabricaDeComunicadoresMasterCard(FabricaDeComunicadores):
    """
    Fabrica de comunicadores do MasterCard.
    """

    def __init__(self):
        """
        Cria as fabricas de emissores e receptores.
        """

        self.__fabrica_de_emissores = FabricaDeEmissores()
        self.__fabrica_de_receptores = FabricaDeReceptores()

    def cria_emissor(self):
        """
        Cria o emissor da MasterCard
        """

        return self.__fabrica_de_emissores.cria(FabricaDeEmissores.MASTERCARD)

    def cria_receptor(self):
        """
        Cria o receptor da MasterCard
        """

        return self.__fabrica_de_receptores.cria(FabricaDeReceptores.MASTERCARD)
