class Acao(object):
    """
    Ação da bolsa de valores
    """

    def __init__(self, codigo, valor):
        """
        Cria a ação da bolsa de valores.
        """

        self.__codigo = codigo
        self.__valor = valor
        self.__observadores = []

    def registra_observador(self, interessado):
        """
        Registra um observador interessado nas mudanças da ação da bolsa.
        """

        self.__observadores.append(interessado)

    def retira_observador(self, interessado):
        """
        Retira um observador interessado nas mudanças da ação da bolsa.
        """

        self.__observadores.remove(interessado)

    @property
    def valor(self):
        """
        Pega o valor da ação.
        """

        return self.__valor

    @valor.setter
    def valor(self, valor):
        """
        Modifica o valor da ação.
        """

        self.__valor = valor

        for interessado in self.__observadores:
            interessado.notifica_alteracao(self)

    @property
    def codigo(self):
        """
        Pega o código da ação da bolsa.
        """

        return self.__codigo
