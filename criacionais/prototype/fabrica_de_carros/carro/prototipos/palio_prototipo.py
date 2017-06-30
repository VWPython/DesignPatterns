from carro.prototipo_de_carro import PrototipoDeCarro


class PalioPrototipo(PrototipoDeCarro):

    def __init__(self, palio=None):
        if palio is None:
            self.valor_da_compra = 0.0
        else:
            self.valor_da_compra = palio.valor_da_compra

    def exibe_informacao(self):
        print("Modelo: Palio")
        print("Montadora: Fiat")
        print("Valor: R$", str(self.valor_da_compra))

    def clonar(self):
        return PalioPrototipo(self)
