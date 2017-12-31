class Historico(object):

    def __init__(self):
        """
        Construtor do histórico do contrato com os estados salvos.
        """

        self.__estados_salvos = []

    def obtem_estado(self, indice):
        """
        Obter o estados do contrato através de um indice
        """

        try:
            estado = self.__estados_salvos[indice]
        except IndexError:
            print("Estado com esse indice não existe.")

        return estado

    def adiciona_estado(self, estado):
        """
        Adiciona o estado atual do contrato na lista de estados
        salvos.
        """

        self.__estados_salvos.append(estado)
