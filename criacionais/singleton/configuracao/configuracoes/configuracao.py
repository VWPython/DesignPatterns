class Configuracao(object):
    """
    Configurações.
    """

    __propriedades = {}
    __instancia = None

    def __init__(self):
        """
        Constroi as configurações caso ainda não exista.
        """

        if self.__instancia is not None:
            raise ValueError("O objeto já existe! utilize a função pega_instancia()")

        self.__propriedades['time-zone'] = "America/Sao_Paulo"
        self.__propriedades['currency-code'] = "BRL"
        self.__propriedades['language'] = "pt-BR"

    @classmethod
    def pega_instancia(self):
        """
        Pega a instância já criada.
        """

        if self.__instancia is None:
            self.__instancia = Configuracao()
        return self.__instancia

    def pega_propriedade(self, nome_da_propriedade):
        """
        Pega as propriedades da configuração.
        """

        return self.__propriedades[nome_da_propriedade]
