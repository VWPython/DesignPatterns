from carro.prototipo_de_carro import PrototipoDeCarro


class PalioPrototipo(PrototipoDeCarro):
    """
    Palio que serve de prótotipo para outros palios.
    """

    def __init__(self, palio=None):
        """
        Cria o prótotipo do palio e se o palio for inserido apenas
        pegue seu valor de compra caso contrário, apenas inicialize ele.
        """

        if palio is None:
            self.valor_da_compra = 0.0
        else:
            self.valor_da_compra = palio.valor_da_compra

    def exibe_informacao(self):
        """
        Mostra informações do palio.
        """

        print("Modelo: Palio")
        print("Montadora: Fiat")
        print("Valor: R$", str(self.valor_da_compra))

    def clonar(self):
        """
        Cria uma cópia exata do palio.
        """

        return PalioPrototipo(self)
