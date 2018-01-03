from pagamentos.bandeiras import ReceptorVisa, ReceptorMasterCard


class FabricaDeReceptores(object):
    """
    Fabrica de receptores.
    """

    VISA = 0
    MASTERCARD = 1

    def cria(self, receptor):
        """
        Cria um receptor.
        """

        if receptor == self.VISA:
            return ReceptorVisa()
        elif receptor == self.MASTERCARD:
            return ReceptorMasterCard()
        else:
            raise Exception("Tipo de receptor não suportado")
