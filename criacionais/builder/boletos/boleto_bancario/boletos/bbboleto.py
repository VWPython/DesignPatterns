from boleto_bancario import Boleto


class BBBoleto(Boleto):
    """
    Boleto do Banco do Brasil.
    """

    def __init__(self, sacado, cedente, valor, vencimento, numero):
        """
        Construtor do boleto.
        """

        self.__sacado = sacado
        self.__cedente = cedente
        self.__valor = valor
        self.__vencimento = vencimento
        self.__numero = numero

    @property
    def sacado(self):
        """
        Pessoa ou empresa resposável pelo pagamento do boleto
        """

        return self.__sacado

    @property
    def cedente(self):
        """
        Pessoa ou empresa que receberá o pagamento do boleto
        """

        return self.__cedente

    @property
    def valor(self):
        """
        Valor do boleto.
        """

        return self.__valor

    @property
    def vencimento(self):
        """
        Vencimento do boleto.
        """

        return self.__vencimento

    @property
    def numero(self):
        """
        Número do boleto.
        """

        return self.__numero

    def imprime(self):
        """
        Imprime o boleto.
        """

        print("Boleto do Banco do Brasil (BB)")
        print("Sacado:", self.sacado)
        print("Cedente:", self.cedente)
        print("Valor:", self.valor)
        print("Vencimento:", self.vencimento)
        print("Número:", self.numero)
