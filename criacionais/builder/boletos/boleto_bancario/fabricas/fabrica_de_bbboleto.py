from boleto_bancario.gerador_de_boleto import GeradorDeBoleto
from boleto_bancario.boletos.bbboleto import BBBoleto


class FabricaDeBBBoleto(GeradorDeBoleto):

    def __init__(self):
        self.__sacado = ''
        self.__cedente = ''
        self.__valor = ''
        self.__vencimento = ''
        self.__numero = ''

    def constroi_sacado(self, sacado):
        self.__sacado = sacado

    def constroi_cedente(self, cedente):
        self.__cedente = cedente

    def constroi_valor(self, valor):
        self.__valor = valor

    def constroi_vencimento(self, vencimento):
        self.__vencimento = vencimento

    def constroi_numero(self, numero):
        self.__numero = numero

    def pega_boleto(self):
        return BBBoleto(self.__sacado, self.__cedente, self.__valor, self.__vencimento, self.__numero)
