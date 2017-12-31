from editor.estado import Estado


class Historico(object):
    """
    Histórico de textos salvos
    """

    def __init__(self):
        """
        Constroi o histórico criando um lista de estados do texto.
        """

        self.__estados = []

    def adiciona_estado(self, estado):
        """
        Adiciona o texto a lista de estados
        """

        self.__estados.append(estado)

    def obtem_ultimo_estado(self):
        """
        Pega o último estado do texto salvo e remove ele da lista
        de estados do texto.
        """

        if (len(self.__estados) > 0):
            estado_salvo = self.__estados[len(self.__estados) - 1]
            self.__estados.pop(len(self.__estados) - 1)
            return estado_salvo
        else:
            return Estado(texto="")
