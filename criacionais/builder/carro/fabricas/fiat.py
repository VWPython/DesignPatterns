from carro.fabricaDeCarros import FabricaDeCarros

class Fiat(FabricaDeCarros):

    def define_preco(self):
        self.carro.preco = 25000.0

    def define_motor(self):
        self.carro.motor = 'Fire Flex 1.0'

    def define_ano_de_fabricacao(self):
        self.carro.ano_de_fabricacao = 2011

    def define_modelo(self):
        self.carro.modelo = 'Palio'

    def define_montadora(self):
        self.carro.montadora = 'Fiat'
