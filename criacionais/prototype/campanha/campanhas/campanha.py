from campanhas.prototipo import Prototipo


class Campanha(Prototipo):
    """
    Objeto Campanha
    """

    def __init__(self, nome, vencimento):
        """
        Constroi a campanha.
        """

        self.__nome = nome
        self.__vencimento = vencimento

    @property
    def nome(self):
        """
        Pega o nome da campanha.
        """

        return self.__nome

    @property
    def vencimento(self):
        """
        Pega o vencimento da campanha.
        """

        return self.__vencimento

    def clone(self):
        """
        Cria um cópia da campanha.
        """

        nome = "Cópia da campanha: %s" % (self.nome)
        vencimento = self.vencimento
        campanha = Campanha(nome, vencimento)
        return campanha

    def imprime(self):
        """
        Imprime a campanha.
        """

        print("--------------")
        print("Nome da Campanha: ", self.nome)
        print("Vencimento:", self.vencimento)
        print("--------------")
