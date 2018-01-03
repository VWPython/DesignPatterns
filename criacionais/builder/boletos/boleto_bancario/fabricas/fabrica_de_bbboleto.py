from boleto_bancario import GeradorDeBoleto
from boleto_bancario.boletos import BBBoleto


class FabricaDeBBBoleto(GeradorDeBoleto):
    """
    Fabrica de boletos do Banco do Brasil.
    """

    def __init__(self):
        """
        Construtor da fábrica.
        """

        self.__sacado = ''
        self.__cedente = ''
        self.__valor = ''
        self.__vencimento = ''
        self.__numero = ''

    def constroi_sacado(self, sacado):
        """
        Insere a pessoa ou empresa responsável pelo pagamento do boleto.
        """

        self.__sacado = sacado

    def constroi_cedente(self, cedente):
        """
        Insere a pessoa ou empresa que receberá o pagamento do boleto.
        """

        self.__cedente = cedente

    def constroi_valor(self, valor):
        """
        Insere o valor do boleto.
        """

        self.__valor = valor

    def constroi_vencimento(self, vencimento):
        """
        Insere o vencimento do boleto.
        """

        self.__vencimento = vencimento

    def constroi_numero(self, numero):
        """
        Insere o número do boleto.
        """

        self.__numero = numero

    def pega_boleto(self):
        """
        Pega o boleto.
        """

        return BBBoleto(
            self.__sacado,
            self.__cedente,
            self.__valor,
            self.__vencimento,
            self.__numero
        )
