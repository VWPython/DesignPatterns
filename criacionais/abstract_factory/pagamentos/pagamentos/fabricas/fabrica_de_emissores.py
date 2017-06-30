from pagamentos.bandeiras.visa import EmissorVisa
from pagamentos.bandeiras.mastercard import EmissorMasterCard


class FabricaDeEmissores(object):

    VISA = 0
    MASTERCARD = 1

    def cria(self, emissor):
        if emissor == self.VISA:
            return EmissorVisa()
        elif emissor == self.MASTERCARD:
            return EmissorMasterCard()
        else:
            raise Exception("Tipo de emissor não suportado")
