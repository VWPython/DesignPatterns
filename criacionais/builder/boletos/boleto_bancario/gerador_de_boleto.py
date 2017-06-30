class GeradorDeBoleto(object):

    def __init__(self, fabrica_de_boletos):
        self.__fabrica_de_boletos = fabrica_de_boletos

    def gera_boleto(self, sacado, cedente, valor, vencimento, numero):
        self.__fabrica_de_boletos.constroi_sacado(sacado)
        self.__fabrica_de_boletos.constroi_cedente(cedente)
        self.__fabrica_de_boletos.constroi_valor(valor)
        self.__fabrica_de_boletos.constroi_vencimento(vencimento)
        self.__fabrica_de_boletos.constroi_numero(numero)

        boleto = self.__fabrica_de_boletos.pega_boleto()

        return boleto
