class FilaDeTrabalho(object):
    """
    Fila de trabalho dos comandos.
    """

    def __init__(self):
        """
        Construtor da fila de trabalho.
        """

        self.__comandos = []

    def adiciona(self, comando):
        """
        Adiciona um comando.
        """

        self.__comandos.append(comando)

    def processa(self):
        """
        Processa os comandos da fila.
        """

        for comando in self.__comandos:
            comando.executa()
