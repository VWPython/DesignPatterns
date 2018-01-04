class BancoDeUsuarios(object):
    """
    Banco de usuários
    """

    __quantidade_de_usuarios = 100
    __usuarios_conectados = 35

    @property
    def numero_de_usuarios(self):
        """
        Pega o número de usuários
        """

        return "Total de usuário: " + str(self.__quantidade_de_usuarios)

    @property
    def usuarios_conectados(self):
        """
        Pega a quantidade de usuários conectados.
        """

        return "Usuários conectados: " + str(self.__usuarios_conectados)
