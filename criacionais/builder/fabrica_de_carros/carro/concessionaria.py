class Concessionaria(object):

    def __init__(self, montadora):
        self.montadora = montadora

    def fabrica_carro(self, preco, ano_de_fabricacao, motor, modelo):
        self.montadora.define_preco(preco)
        self.montadora.define_ano_de_fabricacao(ano_de_fabricacao)
        self.montadora.define_motor(motor)
        self.montadora.define_modelo(modelo)
        self.montadora.define_montadora()

    def disponibiliza_carro(self):
        return self.montadora.constroi_carro()
