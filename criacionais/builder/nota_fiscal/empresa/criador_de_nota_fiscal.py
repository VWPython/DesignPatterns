from datetime import date
from empresa.nota_fiscal import NotaFiscal


class CriadorDeNotaFiscal(object):
    """
    Criador de notas fiscais.
    """

    def __init__(self):
        """
        Construtor da nota fiscal.
        """

        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__itens = None
        self.__detalhes = None

    def com_razao_social(self, razao_social):
        """
        Insere razão social na nota fiscal.
        """

        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        """
        Insere CNPJ na nota fiscal.
        """

        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        """
        Intere data de emissão na nota fiscal.
        """

        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        """
        Insere itens na nota fiscal.
        """

        self.__itens = itens
        return self

    def constroi(self):
        """
        Constroi a nota fiscal.
        """

        if self.__razao_social is None:
            raise Exception('Razão social deve ser preenchida')
        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchida')
        if self.__itens is None:
            raise Exception('Itens deve ser preenchida')
        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()
        if self.__detalhes is None:
            self.__detalhes = ''

        return NotaFiscal(
            razao_social=self.__razao_social,
            cnpj=self.__cnpj,
            data_de_emissao=self.__data_de_emissao,
            itens=self.__itens,
            detalhes=self.__detalhes
        )
