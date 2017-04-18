from carro.fabricaDeCarros import FabricaDeCarros

class Volkswagen(FabricaDeCarros):

    def define_preco(self):
        self.carro.preco = 15000.0

    def define_motor(self):
        self.carro.motor = '1.0 Flex'

    def define_ano_de_fabricacao(self):
        self.carro.ano_de_fabricacao = 2010

    def define_modelo(self):
        self.carro.modelo = 'Gol'

    def define_montadora(self):
        self.carro.montadora = 'Volkswagen'
