from carro.fabricaDeCarros import FabricaDeCarros

class Concessionaria(object):

    def __init__(self, montadora):
        self.montadora = montadora

    def fabrica_carro(self):
        self.montadora.define_preco()
        self.montadora.define_ano_de_fabricacao()
        self.montadora.define_motor()
        self.montadora.define_modelo()
        self.montadora.define_montadora()

    def disponibiliza_carro(self):
        return self.montadora.constroi_carro()
