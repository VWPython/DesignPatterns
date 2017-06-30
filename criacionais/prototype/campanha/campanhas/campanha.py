from campanhas.prototipo import Prototipo


class Campanha(Prototipo):

    def __init__(self, nome, vencimento):
        self.__nome = nome
        self.__vencimento = vencimento

    @property
    def nome(self):
        return self.__nome

    @property
    def vencimento(self):
        return self.__vencimento

    def clone(self):
        nome = "Cópia da campanha: %s" % (self.nome)
        vencimento = self.vencimento
        campanha = Campanha(nome, vencimento)
        return campanha

    def imprime(self):
        print("--------------")
        print("Nome da Campanha: ", self.nome)
        print("Vencimento:", self.vencimento)
        print("--------------")
