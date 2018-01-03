from recursos.compartilha import Compartilha


class Mesa(object):
    """
    Objeto mesa.
    """

    def __init__(self, numero):
        """
        Cria um número de identificação da mesa.
        """

        self.__numero = numero

    @property
    def numero(self):
        """
        Pega o número da mesa.
        """

        return self.__numero


class MesaCompartilhada(Compartilha):
    """
    Mesa compartilhada.
    """

    mesas_disponiveis = []
    mesas_ocupadas = []

    def __init__(self):
        """
        Separa as mesas númeradas em disponiveis e ocupadas.
        """

        self.mesas_disponiveis.append(Mesa(1))
        self.mesas_disponiveis.append(Mesa(7))
        self.mesas_disponiveis.append(Mesa(2))
        self.mesas_disponiveis.append(Mesa(5))
        self.mesas_disponiveis.append(Mesa(10))

        self.mesas_ocupadas.append(Mesa(3))
        self.mesas_ocupadas.append(Mesa(4))
        self.mesas_ocupadas.append(Mesa(6))
        self.mesas_ocupadas.append(Mesa(8))
        self.mesas_ocupadas.append(Mesa(9))

    def adquire(self, numero):
        """
        Adquire a mesa de acordo com o número passado.
        """

        for mesa in self.mesas_disponiveis:
            if mesa.numero == numero:
                print("Mesa adquirida: %s" % mesa.numero)
                self.__ocupar_mesa(mesa)
                return mesa

        print("A mesa número {0} está ocupada no momento".format(numero))

    def libera(self, numero):
        """
        Libera a mesa ocupada para uso.
        """

        for mesa in self.mesas_ocupadas:
            if mesa.numero == numero:
                print("Mesa liberada: %s" % mesa.numero)
                self.__desocupar_mesa(mesa)
                return mesa

        print("A mesa número {0} já foi liberada e está disponivel".format(numero))

    def __ocupar_mesa(self, mesa):
        """
        Ocupa a mesa.
        """

        self.mesas_ocupadas.append(mesa)
        self.mesas_disponiveis.remove(mesa)

    def __desocupar_mesa(self, mesa):
        """
        Desocupa a mesa.
        """

        self.mesas_disponiveis.append(mesa)
        self.mesas_ocupadas.remove(mesa)
