from pagamentos.bandeiras.visa import ReceptorVisa
from pagamentos.bandeiras.mastercard import ReceptorMasterCard


class FabricaDeReceptores(object):

    VISA = 0
    MASTERCARD = 1

    def cria(self, receptor):
        if receptor == self.VISA:
            return ReceptorVisa()
        elif receptor == self.MASTERCARD:
            return ReceptorMasterCard()
        else:
            raise Exception("Tipo de receptor não suportado")
