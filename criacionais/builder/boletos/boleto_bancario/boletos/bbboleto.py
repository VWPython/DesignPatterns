from boleto_bancario.boleto import Boleto


class BBBoleto(Boleto):

    def __init__(self, sacado, cedente, valor, vencimento, numero):
        self.__sacado = sacado
        self.__cedente = cedente
        self.__valor = valor
        self.__vencimento = vencimento
        self.__numero = numero

    @property
    def sacado(self):
        return self.__sacado

    @property
    def cedente(self):
        return self.__cedente

    @property
    def valor(self):
        return self.__valor

    @property
    def vencimento(self):
        return self.__vencimento

    @property
    def numero(self):
        return self.__numero

    def imprime(self):
        print("Boleto do Banco do Brasil (BB)")
        print("Sacado:", self.sacado)
        print("Cedente:", self.cedente)
        print("Valor:", self.valor)
        print("Vencimento:", self.vencimento)
        print("Número:", self.numero)
