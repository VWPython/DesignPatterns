from carro.fabricaDeCarros import FabricaDeCarros


class Fiat(FabricaDeCarros):

    def define_preco(self, preco):
        self.carro.preco = preco

    def define_motor(self, motor):
        self.carro.motor = motor

    def define_ano_de_fabricacao(self, ano_de_fabricacao):
        self.carro.ano_de_fabricacao = ano_de_fabricacao

    def define_modelo(self, modelo):
        self.carro.modelo = modelo

    def define_montadora(self):
        self.carro.montadora = 'Fiat'
