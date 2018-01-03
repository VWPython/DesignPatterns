from datetime import date


class NotaFiscal(object):
    """
    Nota fiscal da empresa.
    """

    def __init__(self, razao_social, cnpj, itens,
                 data_de_emissao=date.today(),
                 detalhes=''):
        """
        Constroi a nota fiscal.
        """

        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = detalhes

    @property
    def razao_social(self):
        """
        Razão social da nota fiscal.
        """

        return self.__razao_social

    @property
    def cnpj(self):
        """
        CNPJ da empresa.
        """

        return self.__cnpj

    @property
    def data_de_emissao(self):
        """
        Data de emissão da nota fiscal
        """

        return self.__data_de_emissao

    @property
    def detalhes(self):
        """
        Detalhes da nota fiscal.
        """

        return self.__detalhes
