class Configuracao(object):

    __propriedades = {}
    __instancia = None

    def __init__(self):
        self.__propriedades['time-zone'] = "America/Sao_Paulo"
        self.__propriedades['currency-code'] = "BRL"
        self.__propriedades['language'] = "pt-BR"

    @classmethod
    def pega_instancia(self):
        if self.__instancia is None:
            self.__instancia = Configuracao()
        return self.__instancia

    def pega_propriedade(self, nome_da_propriedade):
        return self.__propriedades[nome_da_propriedade]
