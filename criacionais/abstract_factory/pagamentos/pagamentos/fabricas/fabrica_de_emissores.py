from pagamentos.bandeiras import EmissorVisa, EmissorMasterCard


class FabricaDeEmissores(object):
    """
    Fabrica de emissores.
    """

    VISA = 0
    MASTERCARD = 1

    def cria(self, emissor):
        """
        Cria emissores.
        """

        if emissor == self.VISA:
            return EmissorVisa()
        elif emissor == self.MASTERCARD:
            return EmissorMasterCard()
        else:
            raise Exception("Tipo de emissor não suportado")
