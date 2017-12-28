from datetime import date


class NotaFiscal(object):
    """
    Classe responsavel pela nota fiscal.
    """

    def __init__(self, razao_social, cnpj, itens,
                 data_de_emissao=date.today(),
                 detalhes='', observadores=[]):
        """
        Cria a nota fiscal.
        """

        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = detalhes
        self.__itens = itens

        # Envia uma notificação para os observadores
        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        """
        Pega a razão social da nota fiscal.
        """

        return self.__razao_social

    @property
    def cnpj(self):
        """
        Pega o CNPJ da nota fiscal.
        """

        return self.__cnpj

    @property
    def data_de_emissao(self):
        """
        Pega a data de emissão da nota fiscal.
        """

        return self.__data_de_emissao

    @property
    def detalhes(self):
        """
        Pega os detalhes da nota fiscal.
        """

        return self.__detalhes
