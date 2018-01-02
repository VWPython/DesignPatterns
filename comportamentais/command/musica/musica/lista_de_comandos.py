class ListaDeComandos(object):
    """
    Lista de comandos para execução.
    """

    def __init__(self):
        """
        Cria a lista de comandos.
        """

        self.__comandos = []

    def adiciona(self, comando):
        """
        Adiciona um comando na lista de comando.
        """

        self.__comandos.append(comando)

    def executa(self):
        """
        Executa a lista de comandos.
        """

        for comando in self.__comandos:
            comando.executa()
